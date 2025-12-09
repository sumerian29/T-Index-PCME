# src/visualize.py

import numpy as np
import matplotlib.pyplot as plt


def show_map(field: np.ndarray, title: str = "", cmap: str = "viridis"):
    """
    Simple helper to display a 2D field.
    """
    plt.figure(figsize=(6, 5))
    plt.imshow(field, origin="lower", cmap=cmap)
    plt.colorbar(label="Value")
    plt.title(title)
    plt.tight_layout()
    plt.show()
