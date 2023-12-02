import numpy as np
import matplotlib.pyplot as plt

def decart_to_cilinder(x: np.array, y: np.array):
    q1 = -np.arctan(x / y)
    q2 = (x ** 2 + y ** 2) ** 0.5 - 0.6
    return q1, q2