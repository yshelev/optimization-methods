f = lambda x: (x - 2) ** 2

def bisection_method(interval: list[float], epsilon: float) -> (float, float):
    """
    метод половинного деления для нахождения минимума с заданной точностью epsilon на интервале interval
    :param interval:
    :param epsilon:
    :return:
    """

    a, b = interval
    delta = epsilon / 3

    while b - a >= epsilon:
        a_k = (a + b) / 2 - delta
        b_k = (a + b) / 2 + delta
        if f(a_k) < f(b_k):
            b = b_k
        else:
            a = a_k
    x_s = (a + b) / 2

    return x_s, f(x_s)

print(bisection_method([-2, 20], 0.005))


