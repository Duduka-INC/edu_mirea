import numpy as np
import matplotlib.pyplot as plt
from transfer import decart_to_cilinder

R = np.array([0.05, 0.04, 0.03])
h = np.array([0.6, 0.6, 0.2])
ro = 2712
m, M = [], []

x = np.array([0.3, 0.5, 0.7, 0.7, 0.6, 0.4, 0.4, 0.3, 0.3])
y = np.array([0.3, 0.3, 0.3, 0.7, 0.5, 0.5, 0.7, 0.5, 0.3]) + 0.4

q1, q2 = decart_to_cilinder(x, y)

for i in range(len(R)):
    m.append(R[i]**2 * h[i] * ro)
    M.append((m[i] * h[i]**2) / 2)

m, M = np.array(m), np.array(M)

print(f'x: {x}\ny: {y}\n')
print(f'q1: {q1.round(2)}\nq2: {q2.round(2)}\n')
print(f'm: {m.round(4)}\nM: {M.round(4)}\n')

plt.grid()
plt.plot(q1, q2)
plt.show()