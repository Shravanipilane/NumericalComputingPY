import math
from Matrix import Matrix


class NumericalIntegrator(Matrix):
    """Parent class: builds the results table.
    The formula itself is written in the child classes."""

    def __init__(self, func, a, b, exact_value, n_values):
        self.func = func
        self.a = a 
        self.b = b
        self.exact_value = exact_value
        self.n_values = n_values
        super().__init__(data=[])

    def is_valid(self, n):
        return True

    def formula(self, y, h):
        raise NotImplementedError("Child class must write formula()")

    def integrate(self, n):
        h = (self.b - self.a) / n
        y = [self.func(self.a + i * h) for i in range(n + 1)]
        return self.formula(y, h)

    def integrate_data(self, y, h):
        return self.formula(y, h)

    def compute_table(self):
        # each row = [n, h, approximation, error]
        for n in self.n_values:
            h = (self.b - self.a) / n
            if not self.is_valid(n):
                self.add_row([n, h, None, None])
            else:
                approx = self.integrate(n)
                self.add_row([n, h, approx, abs(self.exact_value - approx)])
        return self

    def orders(self):
        # order = log(old error / new error) / log(old h / new h)
        result = [None]
        for i in range(1, len(self.data)):
            h_old, err_old = self.data[i - 1][1], self.data[i - 1][3]
            h_new, err_new = self.data[i][1], self.data[i][3]
            if err_old is None or err_new is None or err_old < 1e-12 or err_new < 1e-12:
                result.append(None)
            else:
                result.append(math.log(err_old / err_new) / math.log(h_old / h_new))
        return result


class SimpsonOneThird(NumericalIntegrator):
    """Simpson's 1/3 rule (parabola). n must be even."""

    def is_valid(self, n):
        return n >= 2 and n % 2 == 0

    def formula(self, y, h):
        # h/3 * [ y0 + 4*y1 + 2*y2 + 4*y3 + ... + yn ]
        total = y[0] + y[-1]
        for i in range(1, len(y) - 1):
            if i % 2 == 1:
                total += 4 * y[i]
            else:
                total += 2 * y[i]
        return h / 3 * total


class SimpsonThreeEighth(NumericalIntegrator):
    """Simpson's 3/8 rule (cubic). n must be a multiple of 3."""

    def is_valid(self, n):
        return n >= 3 and n % 3 == 0

    def formula(self, y, h):
        # 3h/8 * [ y0 + 3*y1 + 3*y2 + 2*y3 + 3*y4 + ... + yn ]
        total = y[0] + y[-1]
        for i in range(1, len(y) - 1):
            if i % 3 == 0:
                total += 2 * y[i]
            else:
                total += 3 * y[i]
        return 3 * h / 8 * total 
    
 
