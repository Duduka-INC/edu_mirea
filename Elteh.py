import numpy as np
import matplotlib.pyplot as plt


def calculate_E(Em, fi):
    E = Em/np.sqrt(2)
    real_E = E * np.cos(fi * np.pi/180)
    imag_E = E * np.sin(fi * np.pi/180)
    complex_E = real_E + imag_E * 1j

    return complex_E

def calculate_Xl(L):
    global omega
    return omega * L

def calculate_Xc(C):
    global omega
    return 1 / (omega * C)

def calculate_Z(R = 0, Xl = 0, Xc = 0):
    return R + (Xl - Xc) * 1j

def calculate_Uab(E3 = 0, E5 = 0, Z1 = 0, Z2 = 0, Z3 = 0):
    return ((E3/Z3) + (E5/Z2))/((1/Z1) + (1/Z2) + (1/Z3))

def calculate_Sist(E : np.array, I: np.array):
    sum = 0
    for i in range(len(E)):
        sum += E[i] * np.conj(I[i])
    return sum

def calculate_Spotr(I: np.array, Z: np.array):
    sum = 0
    for i in range(len(I)):
        sum += (abs(I[i])**2 * Z[i])
    return sum

def calculate_fi(z: complex):
    if (z.real < 0 and z.imag < 0):
        return np.arctan(z.imag/z.real) * 180/np.pi - 180
    elif (z.real > 0 and z.imag < 0):
        return np.arctan(z.imag/z.real) * 180/np.pi + 180
    else:
        return np.arctan(z.imag/z.real) * 180/np.pi

R3 = 27
L1 = 0.41
C2 = 77 * 10**(-6)
L5 = 0.63
Em3 = 23
Em5 = 58
fi3 = 220
fi5 = 260
f = 63
omega = 2 * np.pi * f


E3 = calculate_E(Em3, fi3)
E5 = calculate_E(Em5, fi5)
print(f'E3: {E3}\nE5: {E5}\n')


Xl1 = calculate_Xl(L1)
Xl5 = calculate_Xl(L5)
Xc3 = calculate_Xc(C2)

Z1 = calculate_Z(Xl=Xl1)
Z2 = calculate_Z(Xl=Xl5, Xc=Xc3)
Z3 = calculate_Z(R=R3)

print(f'Xl1: {Xl1}\nXl5: {Xl5}\nXc3: {Xc3}\n')
print(f'Z1: {Z1}\nZ2: {Z2}\nZ2: {Z3}\n')


Uab = calculate_Uab(E3, E5, Z1, Z2, Z3)
print(f'Uab: {Uab}\n')

I1 = -Uab/Z1
I2 = (E5 - Uab) / Z2
I3 = (E3 - Uab) / Z3
print(f'I1: {I1}\nI2: {I2}\nI3: {I3}\n')

arrE = np.array([E3, E5])
arrI = np.array([I3, I2])

Sist = calculate_Sist(arrE, arrI)

arrI = np.array([I1, I2, I3])
arrZ = np.array([Z1, Z2, Z3])
Spotr = calculate_Spotr(arrI, arrZ)
print(f'Sist: {Sist}\nSpotr: {Spotr}\n')

S = (Uab * np.conj(I1))
P = S.real

fiUab = calculate_fi(Uab)
fiI1 = calculate_fi(I1)
fi = fiUab - fiI1

absUab = abs(Uab)
absI1 = abs(I1)

print(f'absUab: {absUab}\nabsI1: {absI1}\n')
print(f'fiUab: {fiUab}\nfiI1: {fiI1}\nfi: {fi}\n')

Ui = absUab * absI1 * np.cos(fi * np.pi/180)
print(f'P: {P}\nUi: {Ui.round(12)}')

# plt.polar(fiUab, absUab, 'g.')
# plt.polar(fiI1, absI1, 'r.')

# Vector diag
Vb = 0
Va = Uab
Vt = Vb - Xl1 * I1 * 1j
Vn = Vb + Xl5 * I2 * 1j
Vm = Vn + E5
Vk = Vb - R3 * I3
Vk2 = Va - E3
Vk3 = Uab - E3

print(Vk, Vk2, Vk3)
print(f'Vb: {Vb}\nVa: {Va}\nVt: {Vt}\nVn: {Vn}\nVm: {Vm}\nVk: {Vk}\n')


plt.grid()
plt.quiver(I1.real * 10, I1.imag * 10)
plt.quiver(I2.real * 10, I2.imag * 10)
plt.quiver(I3.real * 10, I3.imag * 10)

plt.quiver(Va.real, Va.imag)
plt.show()