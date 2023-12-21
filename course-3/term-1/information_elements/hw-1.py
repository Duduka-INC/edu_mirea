import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.arange(-0.5, 0.55, 0.05)
U = 76
R = 4800
Rn = 300000

Uout = U * x
Uoutn = U*x*Rn/(R*np.abs(x)+Rn-R*(x)**2)

delta = Uoutn - Uout
sigma = delta / Uout * 100

print(f'Uout: {Uout} \n\nUoutn: {Uoutn}\n')
print(f'delta: {delta} \n\nsigma: {sigma}\n')

plt.figure(figsize=(8, 6), dpi = 200)
plt.grid(which='major', linewidth=1.0)
plt.grid(which='minor', linewidth=0.5)
plt.minorticks_on()
plt.plot(x, Uout, marker='o', label='Uвых0 при разных значениях x')
plt.plot(x, Uoutn, marker='o', label='UвыхH при разных значениях x')
plt.legend()
plt.savefig(r"hw-1/Uвых0_UвыхH.png")
plt.show()

plt.figure(figsize=(8, 6), dpi = 200)
plt.grid(which='major', linewidth=1.0)
plt.grid(which='minor', linewidth=0.5)
plt.minorticks_on()
plt.plot(x, sigma, marker='o', label='Относительная погрешность при разных значениях x')
plt.legend()
plt.savefig(r"hw-1/Относительная_погрешность.png")
plt.show()

plt.figure(figsize=(8, 6), dpi = 200)
plt.grid(which='major', linewidth=1.0)
plt.grid(which='minor', linewidth=0.5)
plt.minorticks_on()
plt.plot(x, delta, marker='o', label='Абсолютная погрешность при разных значениях x')
plt.legend()
plt.savefig(r"hw-1/Абсолютная_погрешность.png")
plt.show()

df = pd.DataFrame({
     "x": x.round(3),
     "Uвых0": Uout.round(3),
     "Uвыхh": Uoutn.round(3),
     "Дельта": delta.round(3),
     "Сигма": sigma.round(3),
     })
df.set_index('x', drop=True, inplace=True)

print(df)
df.to_csv(r"hw-1/table.csv")
df.to_excel(r"hw-1/table.xlsx")