from func import grad

def gradient_descent_method(
    gradient: callable,
    h: float,
    e: float = 10e-6, 
    max_iters: int = 1000
): 
    x_k = [10, 10, 10]

    for i in range(max_iters): 
        gradient = grad(*x_k)
        x_new = x_k - h * gradient
        print(i)

        if vector_norm([x_k[i] - x_new[i] for i in range(3)]) < e: 
            return x_k
    
        x_k = x_new


def vector_norm(x):
    summ = 0

    for i in x: 
        summ += i ** 2
