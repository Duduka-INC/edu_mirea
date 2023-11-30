import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-0.5, 0.55, 0.05)
U = 18
R = 800
Rn = 55000

Uout = U * x
Uoutn = (-U*x*Rn) / (R*x**2 - R*x - Rn)
delta = Uoutn - Uout

sigma = delta / Uout * 100

print(f'Uout: {Uout} \n\nUoutn: {Uoutn}\n')
print(f'delta: {delta} \n\nsigma: {sigma}\n')

plt.grid()
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0, 1].plot(x, Uout, marker='o', label='Uout при разных значениях x')
ax[0, 1].plot(x, Uoutn, marker='o', label='Uoutn при разных значениях x')
ax[1, 0].plot(x, delta, marker='o', label='delta при разных значениях x')
plt.legend()
plt.show() 