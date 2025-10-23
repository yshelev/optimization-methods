import numpy as np

def func(vector: np.array) -> np.float64: 
    return vector[0] ** 2 + (vector[1] - 4) ** 2 + vector[2] ** 2
def grad(vector: np.array) -> np.array: 
    return np.array([2 * vector[0], 2 * (vector[1] - 4), 2 * vector[2]])