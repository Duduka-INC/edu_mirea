import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

U = 45
f = 350
a = 10 * 10**(-3)
b = 50 * 10**(-3)
c = 30 * 10**(-3)
d = 10 * 10**(-3)
dmax = 2 * 10**(-3)
mu = 9000
mu0 = 4 * np.pi * 10**(-7)
omega = 350
q = 1.651
Tyst = 50
deltaT = Tyst - 20
Rh = 2
Kes = 0.9
Ro20grad = 0.0175
alpha = 0.00411
sigma = np.arange(0, 0.0051, 0.005/20)
print(f'len: {len(sigma)}\narray: {sigma}')

Rmc = (2*(b + c) + np.pi * a) / (mu * mu0 * a * d * Kes)
print(f'Rmc: {Rmc}\n')
Rmb = (2*sigma) / (mu0 * a * d)

lwc = 2*a + 2*d + np.pi*b
r = Ro20grad * (((lwc * omega) / q) * (1 + alpha * deltaT))
print(f'lwc: {lwc}\nr: {r}\n')

L = omega**2 / (Rmc + Rmb)
Xl = 2 * np.pi * f * L

I = U / (((Rh + r)**2 + Xl**2)**0.5)
Uout = (U * Rh) / (((Rh + r)**2 + Xl**2)**0.5)

Lid = omega**2 / Rmb
Lreal = omega**2 / (Rmb + Rmc)

XLid = 2 * np.pi * f * Lid
XLreal = 2 * np.pi * f * Lreal

Uout0 = U*Rh/XLid
Uoutreal = U*Rh/np.sqrt((Rh + r)**2 + XLreal**2)

delta2 = Uoutreal - Uout0
errorotn = delta2/Uout0*100

print(f'Rmc: {Rmc} \n\nRmb: {Rmb}\n')
print(f'lwc: {lwc} \n\nr: {r}\n')
print(f'L: {L} \n\nXl: {Xl}\n')
print(f'I: {I} \n\nUout: {Uout}\n')

plt.figure(figsize=(8, 6), dpi = 200)
plt.grid(which='major', linewidth=1.0)
plt.grid(which='minor', linewidth=0.5)
plt.minorticks_on()
plt.plot(sigma, Uout0, marker='o', label='Uвых0 при разных значениях σ')
plt.plot(sigma, Uoutreal, marker='o', label='UвыхH при разных значениях σ')
plt.legend()
plt.savefig(r"hw-2/Uвых0_UвыхH.png")
plt.show()

plt.figure(figsize=(8, 6), dpi = 200)
plt.grid(which='major', linewidth=1.0)
plt.grid(which='minor', linewidth=0.5)
plt.minorticks_on()
plt.plot(sigma, errorotn, marker='o', label='Относительная погрешность при разных значениях σ')
plt.legend()
plt.savefig(r"hw-2/Относительная_погрешность.png")
plt.show()

plt.figure(figsize=(8, 6), dpi = 200)
plt.grid(which='major', linewidth=1.0)
plt.grid(which='minor', linewidth=0.5)
plt.minorticks_on()
plt.plot(sigma, delta2, marker='o', label='Абсолютная погрешность при разных значениях σ')
plt.legend()
plt.savefig(r"hw-2/Абсолютная_погрешность.png")
plt.show()

df = pd.DataFrame({
     "σ": (sigma * 1000).round(3),
     "Uвых идеальное": Uout0.round(3),
     "Uвых реальное": Uoutreal.round(3),
     "Дельта": delta2.round(3),
     "σ Uвых": errorotn.round(3),
     })
df.set_index('σ', drop=True, inplace=True)

print(df)
df.to_csv(r"hw-2/table.csv")
df.to_excel(r"hw-2/table_excel.xlsx")