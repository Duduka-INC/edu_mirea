import numpy as np
import matplotlib.pyplot as plt
from decart_to_cilinder import decart_to_cilinder

x = np.array([0.3, 0.5, 0.7, 0.7, 0.6, 0.4, 0.4, 0.3, 0.3])
y = np.array([0.3, 0.3, 0.3, 0.7, 0.5, 0.5, 0.7, 0.5, 0.3])

print(f'x: {x}\n\ny: {y}\n')

plt.grid()
plt.plot(x, y)
plt.show()