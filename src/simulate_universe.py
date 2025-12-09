# src/simulate_universe.py

import numpy as np


def simulate_universe(n: int = 128, seed: int = 0):
    """
    Simulate a simple 'digital universe' on a 2D grid.

    Returns
    -------
    noise : np.ndarray
        Pure Gaussian noise field.
    signal_map : np.ndarray
        Noise + a radial ring-like signal.
    radius_map : np.ndarray
        Radial index (float) for each pixel measured from the center.
    """
    rng = np.random.default_rng(seed)

    # 1) pure noise
    noise = rng.normal(loc=0.0, scale=1.0, size=(n, n))

    # 2) coordinates and radius
    x = np.arange(n) - (n / 2.0) + 0.5
    y = np.arange(n) - (n / 2.0) + 0.5
    X, Y = np.meshgrid(x, y, indexing="xy")
    radius_map = np.sqrt(X**2 + Y**2)

    # 3) radial ring signal (simple toy model)
    r0 = n * 0.25      # ring radius
    sigma = n * 0.05   # ring thickness
    amplitude = 3.0    # signal strength

    ring = amplitude * np.exp(-((radius_map - r0) ** 2) / (2.0 * sigma**2))

    signal_map = noise + ring

    return noise, signal_map, radius_map
