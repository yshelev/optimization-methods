import numpy as np

A = np.array([
    [5, 1, 2],
    [1, 4, 1],
    [2, 1, 3]
])

B = np.array([
    1, 1, 1
])
def func(x: np.array) -> np.float64: 
    return 0.5 * (x.T @ A @ x) + B.T @ x
def grad(x: np.array) -> np.array: 
    return (A @ x) + B
