# examples/example_run.py

import sys
import os

# add project root to path to import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np

from src.simulate_universe import simulate_universe
from src.tindex import (
    generate_prime_composite_masks,
    compute_T_index,
    compute_PCME,
)
from src.visualize import show_map


def main():
    # 1) simulate digital universe
    print("\n=== Step 1: Simulating Digital Universe ===")
    noise, signal_map, radius_map = simulate_universe()
    k_map = np.rint(radius_map).astype(int)

    # 2) prime/composite masks
    print("\n=== Step 2: Generating Prime / Composite Masks ===")
    prime_mask, comp_mask = generate_prime_composite_masks(k_map)

    # 3) original T-Index
    print("\n=== Step 3: Computing Original T-Index ===")
    T_noise, Cp_noise, Dc_noise = compute_T_index(noise, prime_mask, comp_mask)
    T_signal, Cp_signal, Dc_signal = compute_T_index(signal_map, prime_mask, comp_mask)

    print("\n--- T-Index (Noise only) ---")
    print(f"C_p = {Cp_noise:.6f}")
    print(f"D_c = {Dc_noise:.6f}")
    print(f"T_noise = {T_noise:.6f}")

    print("\n--- T-Index (Noise + Signal) ---")
    print(f"C_p = {Cp_signal:.6f}")
    print(f"D_c = {Dc_signal:.6f}")
    print(f"T_signal = {T_signal:.6f}")

    # 4) PCME
    print("\n=== Step 4: Computing PCME (Prime-Composite Matching Energy) ===")
    E_noise, S_p_noise, S_c_noise = compute_PCME(noise, k_map, k_match_max=24)
    E_signal, S_p_signal, S_c_signal = compute_PCME(signal_map, k_map, k_match_max=24)

    print("\n--- PCME (Noise only) ---")
    print(f"E_match = {E_noise:.6f}")
    print(f"S_prime (sum) = {S_p_noise:.6f}")
    print(f"S_composite (sum) = {S_c_noise:.6f}")

    print("\n--- PCME (Noise + Signal) ---")
    print(f"E_match = {E_signal:.6f}")
    print(f"S_prime (sum) = {S_p_signal:.6f}")
    print(f"S_composite (sum) = {S_c_signal:.6f}")

    print("\n=== Done. ===")


if __name__ == "__main__":
    main()
