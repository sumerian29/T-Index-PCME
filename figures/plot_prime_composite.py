import matplotlib.pyplot as plt
import numpy as np
from sympy import primerange

# generate primes and composites
primes = list(primerange(2, 50))
composites = [n for n in range(4, 50) if n not in primes]

# compute cumulative sums
k = np.arange(1, 15)
S_P = np.cumsum(primes[:14])
S_C = np.cumsum(composites[:14])

plt.figure(figsize=(8,5))
plt.plot(k, S_P, label="Prime Sum", linewidth=3)
plt.plot(k, S_C, label="Composite Sum", linewidth=3)
plt.axvspan(4,7, color='yellow', alpha=0.3)

plt.title("Prime–Composite Early Sum Symmetry")
plt.xlabel("k")
plt.ylabel("Cumulative Sum")
plt.legend()
plt.grid()

plt.savefig("prime_composite_symmetry.png", dpi=300)
plt.show()
print("Saved plot_prime_composite.png successfully")
