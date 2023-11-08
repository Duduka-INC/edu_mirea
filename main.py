import numpy as np
import matplotlib.pyplot as plt

U = 25
f = 350
a = 0.010
b = 0.050
c = 0.030
d = 0.010
dm = 0.002
mu = 7000
mu0 = 4 * np.pi * 10**(-7)
omega = 250
q = 2.378
Tyst = 45
deltaT = Tyst - 20
Rh = 1
Kes = 0.9
Ro20grad = 0.0175
alpha = 0.00411
sigma = np.arange(0, 0.0021, 0.0001)

Rmc = (2*(b + c) + np.pi * a) / (mu * mu0 * a * d * Kes)
Rmc = Rmc * 180 / np.pi
Rmb = (2*sigma) / (mu0 * a * d)

lwc = 2*a + 2*d + np.pi*b
r = Ro20grad * (((lwc * omega) / q) * (1 + alpha * deltaT))

L = omega**2 / (Rmc + Rmb)
Xl = 2 * np.pi * f * L

I = U / (((Rh + r)**2 + Xl**2)**0.5)
Uout = (U * Rh) / (((Rh + r)**2 + Xl**2)**0.5)

print(f'Rmc: {Rmc} \n\nRmb: {Rmb}\n')
print(f'lwc: {lwc} \n\nr: {r}\n')
print(f'L: {L} \n\nXl: {Xl}\n')
print(f'I: {I} \n\nUout: {Uout}\n')

plt.grid()
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0, 0].plot(Rmb, sigma, marker='o', label='Rmb при разных значениях sigma')
ax[0, 1].plot(L, sigma, marker='o', label='L при разных значениях sigma')
ax[0, 1].plot(Xl, sigma, marker='o', label='Xl при разных значениях sigma')
ax[1, 0].plot(I, sigma, marker='o', label='I при разных значениях sigma')
ax[1, 1].plot(Uout, sigma, marker='o', label='Uout при разных значениях sigma')
plt.legend()
plt.show()
