from func import grad, func
import numpy as np

def gradient_descent_method(
    h: float = 2,
    start_point: np.array = np.array([1, 1, 1]), 
    e: float = 10e-18, 
    max_iters: int = 10000
): 
    x_k = start_point

    gradient = grad(x_k)
    x_new = x_k - h * gradient
    change_condition = func(x_new) <= func(x_k)

    for i in range(max_iters): 
        gradient = grad(x_k)
        x_new = x_k - h * gradient
        print(f"""{i}-ая Итерация:
Текущий шаг: {h} 
Текущий вектор x_k: {x_k}
Значение в точке x_k: {func(x_k)}
Градиент в точке x_k: {gradient}
Новое значение x_k: {x_new}, """) 
               

        if sum((x_k - x_new) ** 2) < e: 
            return x_new, func(x_new)
        
        if (func(x_k) <= func(x_new)) != change_condition : 
            h /= 2
        
        x_k = x_new
    
    return x_k, func(x_k)