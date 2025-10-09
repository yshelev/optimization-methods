from bisection_method import bisection_method
from func import f
from golden_ratio_method import golden_ratio_method

print(bisection_method([-2, 20], 0.000005))
print(f)
f.reset()
print(golden_ratio_method([-2, 20], 0.000005))
print(f)