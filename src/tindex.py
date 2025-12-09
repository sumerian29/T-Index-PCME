# src/tindex.py

import numpy as np


EPS = 1e-9


def is_prime(n: int) -> bool:
    """Simple primality test for small n."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(n**0.5) + 1
    for k in range(3, r, 2):
        if n % k == 0:
            return False
    return True


def generate_prime_composite_masks(k_map: np.ndarray, k_max: int | None = None):
    """
    Generate boolean masks for prime and composite radial shells.

    Parameters
    ----------
    k_map : np.ndarray of int
        Integer-valued radial indices for each pixel.
    k_max : int or None
        Maximum shell index to consider. If None, uses k_map.max().

    Returns
    -------
    prime_mask : np.ndarray of bool
    comp_mask  : np.ndarray of bool
    """
    k_int = k_map.astype(int)
    if k_max is None:
        k_max = int(k_int.max())

    # precompute prime/composite flags
    flags_prime = {k: is_prime(k) for k in range(0, k_max + 1)}

    prime_mask = np.zeros_like(k_int, dtype=bool)
    comp_mask = np.zeros_like(k_int, dtype=bool)

    for k in range(2, k_max + 1):
        shell = k_int == k
        if not shell.any():
            continue
        if flags_prime[k]:
            prime_mask |= shell
        else:
            comp_mask |= shell

    return prime_mask, comp_mask


def curl_like(field: np.ndarray) -> np.ndarray:
    """
    A simple curl-like operator for a scalar 2D field.

    We approximate:
        curl_like = dF/dx - dF/dy
    just to have a tensor-like (vorticity-like) quantity.
    """
    gy, gx = np.gradient(field)  # note: np.gradient returns [d/dy, d/dx]
    return gx - gy


def compute_T_index(field: np.ndarray,
                    prime_mask: np.ndarray,
                    comp_mask: np.ndarray):
    """
    Compute the original T-Index using curl-like energy
    on prime vs composite shells.

    Returns
    -------
    T : float
    C_p : float
    D_c : float
    """
    C = np.abs(curl_like(field))

    # avoid empty masks
    if not prime_mask.any() or not comp_mask.any():
        return np.nan, np.nan, np.nan

    C_p = C[prime_mask].mean()
    D_c = C[comp_mask].mean()
    T = C_p / (D_c + EPS)
    return T, C_p, D_c


def compute_PCME(field: np.ndarray,
                 k_map: np.ndarray,
                 k_match_max: int = 24):
    """
    Compute PCME (Prime–Composite Matching Energy) as described.

    Parameters
    ----------
    field : np.ndarray
        2D scalar field.
    k_map : np.ndarray
        Radial index map (integer).
    k_match_max : int
        Maximum shell index to include in the matching.

    Returns
    -------
    E_match : float
    S_prime : float
    S_comp  : float
    """
    C = np.abs(curl_like(field))
    k_int = k_map.astype(int)

    # accumulate shell energies S_k
    S_k = {}
    for k in range(2, k_match_max + 1):
        shell = k_int == k
        if not shell.any():
            continue
        S_k[k] = float(C[shell].sum())

    # total prime and composite energy
    S_prime = 0.0
    S_comp = 0.0
    for k, val in S_k.items():
        if is_prime(k):
            S_prime += val
        else:
            S_comp += val

    E_match = 1.0 - abs(S_prime - S_comp) / (S_prime + S_comp + EPS)
    return E_match, S_prime, S_comp
