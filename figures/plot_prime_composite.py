import numpy as np
import matplotlib.pyplot as plt

# simple prime/composite generation
def is_prime(n: int) -> bool:
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

nums = list(range(2, 50))
primes = [n for n in nums if is_prime(n)]
composites = [n for n in nums if not is_prime(n)]

k = np.arange(1, len(primes) + 1)
S_P = np.cumsum(primes[:len(k)])
S_C = np.cumsum(composites[:len(k)])

plt.figure(figsize=(8,5))
plt.plot(k, S_P, label="Prime cumulative sum", linewidth=2)
plt.plot(k, S_C, label="Composite cumulative sum", linewidth=2)
# highlight the early symmetry region manually (k ~ 3..7 depends on definition)
plt.axvspan(3.5, 7.5, alpha=0.3)
plt.xlabel("Index k")
plt.ylabel("Cumulative sum")
plt.title("Early Prime–Composite Sum Symmetry (Conceptual)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("prime_composite_sums.png", dpi=300)
plt.show()
