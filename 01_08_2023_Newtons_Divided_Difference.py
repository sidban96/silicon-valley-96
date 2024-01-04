import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, Eq, solve


x_values=[1,2,3,4,5]
y_values=np.sin(x_values)
x=sp.symbols('x')
y=sp.symbols('y')
c=[]
plt.plot(x_values, y_values)

rows=len(x_values)
cols=len(x_values)



print("We will try to make the preferred matrix in a way which we can access")
print("It will be a lower triangular matrix as shown below")

print("Initialize an empty matrix")
matrix = [[1 for _ in range(cols)] for _ in range(rows)]


# Create a lower triangular matrix
for i in range(rows):
    for j in range(rows):
        if j <= i:
            matrix[i][j]=matrix[i][j]*(x-x_values[j])  # You can replace this with any value
        else:
            continue
    

# Print the lower triangular matrix
for row in matrix:
    print(row)

print("Now we consider the last row of this matrix and save it in an array")


# Choose the row index you want to save
row_index = rows-1

# Save the row as a 1D array
row_array = matrix[row_index]


# Print the saved row array
print(row_array)

n=len(row_array)


print("Now we save the array according our need in a matrix")
#print("p4(x) = −5 + 2x − 4x(x − 1) + 8x(x − 1)(x + 1) + 3x(x − 1)(x + 1)(x − 2)")

matrix = [[1 for _ in range(cols)] for _ in range(rows)]

for i in range(n):
    for j in range(n):
        if i==j:
            matrix[i][j]*=row_array[j]

for row in matrix:
    print(row)

print("Now we save the array according our need in a matrix")

mul=1
for i in range(n):
    for j in range(n):
        if j<=i:
            mul*=matrix[i][j]
            matrix[i][j]=mul

for row in matrix:
    print(row)



for i in range(n):
    for j in range(n):
        if i==j:
            print(matrix[i][j])
            row_array[i]=matrix[i][j]

row_array1=row_array
# Create a list of symbolic expressions with c coefficients
coefficients = [sp.Symbol(f'c{i}') for i in range(n)]


sum_1=0
for i in range(n):
        solve=coefficients[i]*row_array[i]
        sum_1+=solve
        row_array[i]=sum_1

print(row_array)

# Define values for x to evaluate the expressions
x_values_for_evaluation = [1,2,3,4,5]

# Evaluate the symbolic expressions for the given x values
evaluated_results = [sum_1.subs(x, val+1) for val in x_values_for_evaluation]

print("Results for the given x values:", evaluated_results)




'''

print("Upto here we have got the individual values of the various stages of the equation")

print("Now we have to get the values of the individual 'c' in the above equation")

print("For that we start again")


print("We will try to make the preferred matrix in a way which we can access")
print("It will be a lower triangular matrix as shown below")

print("Initialize an empty matrix")
matrix = [[1 for _ in range(cols)] for _ in range(rows)]


# Create a lower triangular matrix
for i in range(rows):
    for j in range(1,rows):
        if j <= i:
            matrix[i][j]=matrix[i][j]*(x_values[i]-x_values[j])  # You can replace this with any value
        else:
            continue
    

# Print the lower triangular matrix
for row in matrix:
    print(row)

print("Now we consider the last row of this matrix and save it in an array")


# Choose the row index you want to save
row_index = rows-1

# Save the row as a 1D array
row_array = matrix[row_index]


# Print the saved row array
print(row_array)

n=len(row_array)


print("Now we save the array according our need in a matrix")
print("p4(x) = −5 + 2x − 4x(x − 1) + 8x(x − 1)(x + 1) + 3x(x − 1)(x + 1)(x − 2)")

matrix = [[1 for _ in range(cols)] for _ in range(rows)]

for i in range(n):
    for j in range(n):
        if i==j:
            matrix[i][j]*=row_array[j]

for row in matrix:
    print(row)

print("Now we save the array according our need in a matrix")

mul=1
for i in range(n):
    for j in range(n):
        if j<=i:
            mul*=matrix[i][j]
            matrix[i][j]=mul

for row in matrix:
    print(row)



for i in range(n):
    for j in range(n):
        if i==j:
            print(matrix[i][j])
            row_array[i]=matrix[i][j]

row_array1=row_array


print("As the first number is multiplied with 1 we have added in array")





for i in range(n):
        x=x_values[i]
        solve=y_values[0]+c*row_array[i]
        row_array[i]=solve

print(row_array)


'''




















