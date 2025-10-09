class F:
	count: int = 0

	def __call__(self, x: float) -> float:
		self.count += 1
		return self._func(x)

	def reset(self):
		self.count = 0

	def _func(self, x: float) -> float:
		return (x - 2) ** 2

	def __str__(self):
		return str(self.count)

f = F()