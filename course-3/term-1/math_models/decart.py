import numpy as np
import matplotlib.pyplot as plt

r = 0.05
l = 0.6
m = 8
J = (m * r**2) / 2

x = np.array([0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 0.5])
y = np.array([0.5, 0.8, 0.8, 0.7, 0.7, 0.6, 0.6, 0.5, 0.5])

print(f"J: {J}\n")
print(f'x: {x}\ny: {y}\n')

plt.grid()
plt.plot(x, y)
plt.show()