import matplotlib.pyplot as plt
import numpy as np
import os
os.system('cls')

def compute_bezier_point(t, control_points):
    n = len(control_points) - 1
    point = np.zeros_like(control_points[0], dtype=float)  # Ensure point data type matches
    for i in range(n + 1):
        point += control_points[i] * binomial_coefficient(n, i) * (1 - t)**(n - i) * t**i
    return point

def binomial_coefficient(n, k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))

def plot_bezier_curve(control_points, num_points=1000):
    t_values = np.linspace(0, 1, num_points)
    curve_points = np.array([compute_bezier_point(t, control_points) for t in t_values])

    plt.plot(curve_points[:, 0], curve_points[:, 1], label='Bezier Curve')
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')

    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bezier Curve')
    plt.grid(True)
    plt.show()

# Example control points
control_points = np.array([
    [1, 9],
    [2, 5],
    [5, 4],
    [7, 8]
])

plot_bezier_curve(control_points)
