from gradient_descent_method import gradient_descent_method
import numpy as np

x_k, f_xk = gradient_descent_method()

print("вектор X: ")
for i in x_k: 
    print(f'{i:.4f}')

print("Значение в (.) X: ")
print(f_xk)