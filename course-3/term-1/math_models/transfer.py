import numpy as np

def decart_to_cilinder(x: np.array, y: np.array):
    q1 = -np.arctan(x / y)
    q2 = (x ** 2 + y ** 2) ** 0.5 - 0.6

    return q1, q2

def decart_to_scara(x: np.array, y: np.array):
    a = np.arctan(y/x)
    r = np.sqrt(x**2 + y**2)

    g1 = np.arccos((6**2 + r**2 - 5**2) / (2*6*r))
    g2 = np.arccos((6**2 + 5**2 - r**2) / (2*6*5))

    q1 = -np.pi/2 + a + g1
    q2 = - np.pi + g2

    return q1, q2