import matplotlib.pyplot as plt
import numpy as np

labels = ["Noise", "Noise + Signal"]

pcme = [0.6656, 0.6907]
tindex = [0.994, 0.998]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(8,5))
plt.bar(x - width/2, tindex, width, label="T-Index")
plt.bar(x + width/2, pcme, width, label="PCME")

plt.ylabel("Metric Value")
plt.title("PCME vs T-Index Sensitivity")
plt.xticks(x, labels)
plt.grid(axis='y')
plt.legend()

plt.savefig("pcme_vs_tindex.png", dpi=300)
plt.show()
