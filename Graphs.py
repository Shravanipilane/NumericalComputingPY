import numpy as np 
import matplotlib.pyplot as plt
from Interpolator import LagrangeInterpolation

def plot_interpolation(x_data, y_data, estimate_points, title):
    interp = LagrangeInterpolation(x_data, y_data)

    # smooth curve
    x_curve = np.linspace(min(x_data), max(x_data), 200)
    y_curve = [float(interp.estimate(v)) for v in x_curve]

    plt.figure()
    plt.plot(x_curve, y_curve, label="Interpolation curve")
    plt.scatter(x_data, y_data, color="black", zorder=5, label="Given data")

    for point in estimate_points:
        y_point = float(interp.estimate(point))
        plt.scatter([point], [y_point], color="red", zorder=6, label="Estimate")
        # write the answer right next to the red dot
        plt.annotate(f"({point}, {y_point:.3f})",
                     (point, y_point),
                     textcoords="offset points", xytext=(10, 10),
                     color="red", fontsize=9, fontweight="bold")

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_interpolation([0, 1, 2], [1, 3, 7], [1.5], "Question 1")
    plot_interpolation([1, 2, 3, 4], [2.0, 4.5, 8.0, 13.5], [2.5, 3.5], "Question 2")
    plot_interpolation([0, 0.5, 1.5, 3], [1.000, 1.125, 1.875, 4.000], [1, 2], "Question 3")
    plot_interpolation([2, 3, 5, 7], [5, 10, 26, 50], [4, 6, 8], "Question 4")
    plot_interpolation([1, 2, 3, 4], [1, 4, 9, 16], [], "Question 5")