# Exercise 2.6
# Soal: Berdasarkan Example 2.14 dan 2.15, buat program yang mem-plot
# beberapa fungsi matematika sekaligus dalam satu grafik dengan warna
# berbeda, lengkap dengan legend:
#   y = 3x + 4
#   y = 2x^2 + 1
#   y = x^3 + 9

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y1 = 3 * x + 4
y2 = 2 * x**2 + 1
y3 = x**3 + 9

plt.plot(x, y1, color='blue',  label='y = 3x + 4')
plt.plot(x, y2, color='red',   label='y = 2x^2 + 1')
plt.plot(x, y3, color='green', label='y = x^3 + 9')

plt.title('Multiple Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
