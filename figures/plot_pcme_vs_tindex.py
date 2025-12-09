import numpy as np
import matplotlib.pyplot as plt

labels = ["Noise", "Noise + Signal"]
pcme = [0.6656, 0.6907]
tindex = [0.9940, 0.9980]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(7,5))
ax.bar(x - width/2, tindex, width, label="T-Index")
ax.bar(x + width/2, pcme, width, label="PCME")

ax.set_ylabel("Metric value")
ax.set_title("PCME vs T-Index sensitivity")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis="y")

plt.tight_layout()
plt.savefig("pcme_vs_tindex.png", dpi=300)
plt.show()
