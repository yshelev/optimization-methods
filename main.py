from bisection_method import bisection_method
from func import f
from golden_ratio_method import golden_ratio_method


interval = [-20, 9]
epsilon = 0.005
print(bisection_method(interval, epsilon))
print(f)
f.reset()
print(golden_ratio_method(interval, epsilon))
print(f)