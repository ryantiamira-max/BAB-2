# Example 2.15 - THE PLOT2.PY PROGRAM
# Plot sin(x) dan cos(x) sekaligus, dengan warna, marker, dan legend

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, color='blue', marker="s", label='Sin')
plt.plot(x, y2, color='red', marker="o", label='Cos')
plt.legend()
plt.show()
