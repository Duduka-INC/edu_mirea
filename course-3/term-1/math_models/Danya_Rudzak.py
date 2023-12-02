import numpy as np
import matplotlib.pyplot as plt
from decart_to_cilinder import decart_to_cilinder

x = np.array([0.35, 0.35, 0.45, 0.55, 0.65, 0.65, 0.55, 0.45, 0.35])
y = np.array([0.45, 0.55, 0.65, 0.65, 0.55, 0.45, 0.35, 0.35, 0.45])

plt.grid()
plt.plot(x, y)
plt.show()

q1, q2 = decart_to_cilinder(x, y)

print(f'x: {x}\n\ny: {y}\n')
print(f'q1: {q1}\n\nq2: {q2}\n')

plt.grid()
plt.plot(q1, q2)
plt.show()
