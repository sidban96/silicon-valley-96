import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, Eq, solve

x_values = [3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
y_values = [9.0, 16.0 , 25.0, 36.0, 49.0, 64.0]
plt.plot(x_values, y_values)

t = sp.symbols('t')

print("Now for the x values")
n = len(x_values)
rows=n-1
cols=n-1

p_1_x = [[1 for _ in range(cols)] for _ in range(rows)]
x_save=[]
#for k in range (n-1) : 
#print("Stage"+str(k))
for i in range (rows):
    for j in range(cols):  # Use n - 1 since you're comparing with the next element
       p_1_x[i][j] = x_values[j] + (x_values[j + 1] - x_values[j]) * t
       x_values[j] =p_1_x[i][j]

print("Printing the x-matrix for our method")
for i in range(rows):
    for j in range(cols):
        print(f"<{i}, {j}>: {p_1_x[i][j]}", end="  ")
    print() 
    
print("Now to extract the end equation")

solve_x=p_1_x[n-2][0]
sp.pprint(solve_x)

print("Generate t values using numpy.linspace")
t_values = np.linspace(0, 1, num=500)  # Generate 11 values between 0 and 1
print(t_values)
print(" Substitute t values and solve")

x_calc=[]
for t_val in t_values:
    solution = solve_x.subs(t, t_val)
    x_calc.append(solution)
    print(f"t = {t_val:.2f}: Solution = {solution:.4f}")

print(x_calc)



print("Now for the y values")

p_1_y = [[1 for _ in range(cols)] for _ in range(rows)]

#for k in range (n-1) : 
#print("Stage"+str(k))
for i in range (rows):
    for j in range(cols):  # Use n - 1 since you're comparing with the next element
       p_1_y[i][j] = y_values[j] + (y_values[j + 1] - y_values[j]) * t
       y_values[j] =p_1_y[i][j]
       
print("Printing the y-matrix for our method")
for i in range(rows):
    for j in range(cols):
        print(f"<{i}, {j}>: {p_1_y[i][j]}", end="  ")
    print() 
    
print("Now to extract the end equation")

solve_y=p_1_y[n-2][0]
sp.pprint(solve_y)

print("Generate t values using numpy.linspace")

print(" Substitute t values and solve")

y_calc=[]
for t_val in t_values:
    solution = solve_y.subs(t, t_val)
    y_calc.append(solution)
    print(f"t = {t_val:.2f}: Solution = {solution:.4f}")

print(y_calc)

plt.plot(x_calc,y_calc)




'''
# Combine x_calc and y_calc into a single numpy array
data = np.column_stack((x_calc, y_calc))
print(data)


import csv


# Specify the file name
csv_file = "output_data.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x_calc', 'y_calc'])  # Write header row
    writer.writerows(data)      # Write the data rows

print(f"Data written to {csv_file}")


x_values = [1.0, 2.0, 3.0, 7.0,9.0]
y_values = [3.0,6.0,9.0,49.0,81.0]

# Combine x_calc and y_calc into a single numpy array
data = np.column_stack((x_values, y_values))
print(data)

# Specify the file name
csv_file = "output_data_1.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x_values', 'y_values'])  # Write header row
    writer.writerows(data)      # Write the data rows

print(f"Data written to {csv_file}")




'''