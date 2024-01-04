import os
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

os.system('cls')

# Sample data points
x = np.array([1, 2, 3, 9, 5])
y = np.array([3, 9, 18, 32, 50])

# Fit a polynomial of degree 2 (quadratic) to the data
coefficients = np.polyfit(x, y, 2)

# Generate a polynomial function based on the coefficients
poly_function = np.poly1d(coefficients)

# Generate x values for the fitted polynomial curve
x_fit = np.linspace(min(x), max(x), 100)

# Calculate corresponding y values using the polynomial function
y_fit = poly_function(x_fit)

# Plot the original data and the fitted polynomial curve
plt.scatter(x, y, label='Data')
plt.plot(x_fit, y_fit, label='Fitted Polynomial', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Polynomial Fitting')
plt.show()

# Display the coefficients of the fitted polynomial
print("Fitted Polynomial Coefficients:", coefficients)