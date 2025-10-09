import math


def golden_ratio_method(interval: list[int], epsilon: float):
	lambda_ = (math.sqrt(5) - 1) / 2
	a, b = interval

	a_k = a + (1 - lambda_) * (b - a)
	b_k = a + lambda_ * (b - a)