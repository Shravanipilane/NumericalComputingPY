from Matrix import Matrix

class Interpolator(Matrix):
    
    def __init__(self, x_values, y_values):
        # Reuse Matrix's __init__ to store the raw data table.
        super().__init__([list(x_values), list(y_values)])
        self.x_values = list(x_values)
        self.y_values = list(y_values)


class LagrangeInterpolation(Interpolator):

    def basis(self, i, x_value):
        """Value of the i-th Lagrange basis term L_i at x_value."""
        xi = self.x_values 
        L = 1
        for j in range(len(xi)):
            if j != i:
                L *= (x_value - xi[j]) / (xi[i] - xi[j])
        return L

    def estimate(self, x_value): 
        """Estimate f(x_value) = sum(y_i * L_i(x_value))."""
        total = 0
        for i in range(len(self.x_values)):
            total += self.y_values[i] * self.basis(i, x_value)
        return total

    def find_degree(self):
        diffs = list(self.y_values)
        order = 0
        while len(diffs) > 1:
            diffs = [diffs[k + 1] - diffs[k] for k in range(len(diffs) - 1)]
            order += 1
            if all(abs(d - diffs[0]) < 1e-9 for d in diffs):
                return order
        return order 