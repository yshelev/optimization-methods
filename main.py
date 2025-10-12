from bisection_method import bisection_method
from func import f
from golden_ratio_method import golden_ratio_method

print(bisection_method([-20, 9], 0.0005))
print(f)
f.reset()
print(golden_ratio_method([-20, 9], 0.0005))
print(f)