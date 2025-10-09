from func import f

def bisection_method(interval: list[float], epsilon: float) -> (float, float, int):
    """
    Метод половинного деления для нахождения минимума с заданной точностью epsilon на интервале interval
    :param interval:
    :param epsilon:
    :return:
    """

    a, b = interval
    delta = epsilon / 3
    iteration = 0

    while b - a >= epsilon:
        iteration += 1
        a_k = (a + b) / 2 - delta
        b_k = (a + b) / 2 + delta
        if f(a_k) < f(b_k):
            b = b_k
        else:
            a = a_k
    x_s = (a + b) / 2

    return x_s, f(x_s), iteration
