import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, t):
    n = len(x)
    result = 0
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (t - x[j]) / (x[i] - x[j])
        result += term
    
    return result

# Example data points
x_values = [1, 2, 3, 4]
y_values = [2, 3, 5, 8]

# Value to interpolate at
t_value = 2.5

# Calculate the interpolated value using Lagrange interpolation
interpolated_value = lagrange_interpolation(x_values, y_values, t_value)

# Plot the data points and the interpolation
plt.scatter(x_values, y_values, color='blue', label='Data Points')
plt.axvline(x=t_value, color='red', linestyle='--', label=f'Interpolation at t = {t_value:.2f}')
plt.plot(t_value, interpolated_value, marker='o', color='red', markersize=8, label='Interpolated Value')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()




