import math

class F:
	count: int = 0

	def __call__(self, x: float) -> float:
		self.count += 1
		return self._func(x)

	def reset(self):
		self.count = 0

	def _func(self, x: float) -> float:
		return (0.5 * x - 5) ** 3 * math.e ** (x / 4)

	def __str__(self):
		value = self.count
		self.reset()
		return f"Количество вызовов функции: {str(value)}"

f = F()