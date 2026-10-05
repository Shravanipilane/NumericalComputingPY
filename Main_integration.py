import math
from Integrator import SimpsonOneThird, SimpsonThreeEighth

# names used in the input file
FUNCTIONS = {
    "X2": lambda x: x ** 2,
    "GAUSS": lambda x: math.exp(-x ** 2),     # e^(-x^2)
}
METHODS = {
    "ONE_THIRD": SimpsonOneThird,             # Simpson's 1/3 rule
    "THREE_EIGHTH": SimpsonThreeEighth,       # Simpson's 3/8 rule
}


def read_questions(filename):
    questions = []
    q = None
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("QUESTION"):
                q = {"title": line, "function": None, "a": 0, "b": 0,
                     "exact": None, "n": [], "x": [], "y": [], "method": ""}
                questions.append(q)
            elif line.startswith("FUNCTION:"):
                q["function"] = line[9:].strip().upper()
            elif line.startswith("A:"):
                q["a"] = float(line[2:])
            elif line.startswith("B:"):
                q["b"] = float(line[2:])
            elif line.startswith("EXACT:"):
                q["exact"] = float(line[6:])
            elif line.startswith("N:"):
                q["n"] = [int(v) for v in line[2:].split()]
            elif line.startswith("X:"):
                q["x"] = [float(v) for v in line[2:].split()]
            elif line.startswith("Y:"):
                q["y"] = [float(v) for v in line[2:].split()]
            elif line.startswith("METHOD:"):
                q["method"] = line[7:].strip().upper()
    return questions


def show(value):
    return "n/a" if value is None else f"{value:.8f}"


def solve_function(q, out):
    rule = METHODS[q["method"]](FUNCTIONS[q["function"]], q["a"], q["b"], q["exact"], q["n"])
    rule.compute_table()
    orders = rule.orders()
    out.write(f"Function: {q['function']}, from {q['a']} to {q['b']}, reference value = {q['exact']}\n")
    out.write(f"{'n':>4} {'h':>12} {'Approx':>14} {'Error':>14} {'Order':>7}\n")
    for row, order in zip(rule.data, orders):
        n, h, approx, error = row
        order_text = "-" if order is None else f"{order:.2f}"
        out.write(f"{n:>4} {show(h):>12} {show(approx):>14} {show(error):>14} {order_text:>7}\n")


def solve_data(q, out):
    x, y = q["x"], q["y"]
    n = len(y) - 1
    h = x[1] - x[0]
    rule = METHODS[q["method"]](None, x[0], x[-1], None, [])
    out.write(f"x = {x}\ny = {y}\nn = {n}, h = {h}\n")
    if rule.is_valid(n):
        out.write(f"Integral = {rule.integrate_data(y, h):.6f}\n")
    else:
        out.write(f"This rule cannot be used with n = {n}\n")


if __name__ == "__main__":
    questions = read_questions("Input_Integration.txt")
    with open("Output_Integration.txt", "w") as out:
        for q in questions:
            out.write(f"\n===== {q['title']} ({q['method']}) =====\n")
            if q["function"]:
                solve_function(q, out)
            else:
                solve_data(q, out)
    print("Done. Results written to Output_Integration.txt")