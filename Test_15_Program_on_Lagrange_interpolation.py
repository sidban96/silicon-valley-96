import os
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from fractions import Fraction
os.system('cls')

# Generate 10 points on a sine curve
x_values = np.linspace(0, 2*np.pi, 3)
y_values = np.sin(x_values)
print(x_values)
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

# Now lets start with our Lagrange Polynomial method

n=len(y_values)
print(n)


# Define the symbolic variable
x = sp.symbols('x')
# Define the quadratic equation
numx=[]  
denx=[]

num=1

for j in range(n):
    num*= (x-x_values[j])
    numx.append(num)
    if j!=n:
        print("..")
print(numx)

# Create a 2D matrix of size rows x cols and fill it with zeros
rows = 3
cols = 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Fill the matrix with values
value = 1
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = x_values[j]
        

# Print the matrix
for row in matrix:
    print(row)

for i in range(rows):
    save=[]
    for j in range(cols):
        if i!=j:
           save[jq]=matrix[i][j]
        else:
            print("skip")
             
    
print(numx)


            
"""    

# Solve the equation for its roots
roots = sp.solve(equation, x)

# Print the roots
print("Roots:", roots)
"""