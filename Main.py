from Testfunctions import FUNCTIONS
from Differentiator import ForwardDifference, BackwardDifference, CentralDifference

x0 = 1
h_values = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5, 10**-6]

methods = [
    ("Forward Difference", ForwardDifference),
    ("Backward Difference", BackwardDifference),
    ("Central Difference", CentralDifference),
]

for func_name, func, exact_value in FUNCTIONS:
    print(f"\n===== f(x) = {func_name} =====")
    for method_name, method_class in methods:
        print(f"\n-- {method_name} --")
        obj = method_class(func, exact_value, x0, h_values) 
        obj.compute_table()
        print("h            approx        error")
        print(obj) 