from Matrix import Matrix

class NumericalDifferentiator(Matrix):
    """Parent class: knows HOW to build the results table.
    Does NOT know which formula to use — that's left to the subclasses."""

    def __init__(self, func, exact_value, x0, h_values):
        self.func = func
        self.exact_value = exact_value
        self.x0 = x0
        self.h_values = h_values
        super().__init__(data=[])  # start empty, fill it in compute_table()

    def diff(self, h): 
        # Subclasses MUST override this. Base class doesn't know the formula.
        raise NotImplementedError("Subclass must implement diff()")

    def compute_table(self):
        for h in self.h_values:
            approx = self.diff(h)
            error = abs(self.exact_value - approx)
            self.add_row([h, approx, error])
        return self


class ForwardDifference(NumericalDifferentiator):
    def diff(self, h):
        return (self.func(self.x0 + h) - self.func(self.x0)) / h

class BackwardDifference(NumericalDifferentiator):
    def diff(self, h):
        return (self.func(self.x0) - self.func(self.x0 - h)) / h

class CentralDifference(NumericalDifferentiator):
    def diff(self, h):
        return (self.func(self.x0 + h) - self.func(self.x0 - h)) / (2 * h)           