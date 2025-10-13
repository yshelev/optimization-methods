from func import f
from utils import print_iterations


def bisection_method(interval: list[float], epsilon: float) -> tuple[float, float, int]:
    """
    Метод половинного деления для нахождения минимума с заданной точностью epsilon на интервале interval
    :param interval:
    :param epsilon:
    :return:
    """

    iterations: list = []

    a, b = interval
    delta = epsilon / 3
    iteration = 0

    while b - a >= epsilon:
        a_k = (a + b) / 2 - delta
        b_k = (a + b) / 2 + delta
        iterations.append({
            "alpha": a_k,
            "betta": b_k,
            "a": a,
            "b": b,
            "len": b - a,
            "iteration": iteration
        })
        iteration += 1
        if f(a_k) < f(b_k):
            b = b_k
        else:
            a = a_k

    x_s = (a + b) / 2
    
    print_iterations(
        iterations, 
    )

    return x_s, f(x_s), iteration
