import math

# Each entry: name, function, exact derivative value at x0 = 1

FUNCTIONS = [
    ("e^x", lambda x: math.exp(x), math.exp(1)),          # f'(x) = e^x
    ("sin(x)", lambda x: math.sin(x), math.cos(1)),        # f'(x) = cos(x)
    ("x^3 - 2x + 1", lambda x: x**3 - 2*x + 1, 3*(1**2) - 2),  # f'(x) = 3x^2 - 2
] 
