from func import grad, func
import numpy as np

def gradient_descent_method(
    h: float,
    e: float = 10e-18, 
    max_iters: int = 1000
): 
    x_k = np.array([10, 10, 10])

    for i in range(max_iters): 
        gradient = grad(x_k)
        print(gradient)
        x_new = x_k - h * gradient
        print(i, x_new, h) 

        if sum((x_k - x_new) ** 2) < e: 
            return x_k
        
        if func(x_k) <= func(x_new): 
            h /= 2
        
        x_k = x_new
    
    return x_k