import math
from func import f


def golden_ratio_method(interval: list[int], epsilon: float) -> (float, float, int):
	"""
	Метод золотого сечения для поиска минимума на интервале interval с заданной точностью epsilon
	:param interval:
	:param epsilon:
	:return:
	"""
	str_lambda = (math.sqrt(5) - 1) / 2
	inv_lambda = (3 - math.sqrt(5)) / 2
	a, b = interval

	iteration = 0

	f_ak = 0
	f_bk = 0

	a_k = a + inv_lambda * (b - a)
	b_k = a + str_lambda * (b - a)

	while b - a >= epsilon:
		iteration += 1
		f_ak = f(a_k) if f_ak == 0 else f_ak
		f_bk = f(b_k) if f_bk == 0 else f_bk

		if f_ak < f_bk:
			b = b_k
			b_k = a_k
			a_k = a + inv_lambda * (b - a)
			f_bk = f_ak
			f_ak = 0
		else:
			a = a_k
			a_k = b_k
			b_k = a + str_lambda * (b - a)
			f_ak = f_bk
			f_bk = 0

	x_s = (a + b) / 2
	return x_s, f(x_s), iteration