import os
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from fractions import Fraction
os.system('cls')

# Generate points on a sine curve
x_values = [1,4,7,9]
y_values = np.sin(x_values)
print(x_values)
print(y_values)

"""print(x_values)
print(y_values)

# Plot the data
plt.scatter(x_values,y_values, label='x and y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('x and y')

# Add legend
plt.legend()

# Show the plot
plt.show()
"""
# Define the symbolic variable
x = sp.symbols('x')
a=[]
eq=[]
for i in range(len(y_values)):
 for j in range(len(y_values)):
  a[j]=y_values[j]
  eq[j]= a[j]
  
 

