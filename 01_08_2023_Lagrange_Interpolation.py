import numpy as np
import matplotlib.pyplot as plt
import sympy as sp




#Data Point Included

x_values = np.linspace(-10, 10, 100)
y_values=(x_values**3+x_values**2+x_values*10+6)

n=len(x_values)

# Define the dimensions of the matrix
rows = n
cols = n

print("I will try the save the equations in an matrix format ")


from CEN_FUNC_FILE import mat_inp
matrix=mat_inp(n,x_values,rows,cols)


print("For accessing the matrix for our work. In here we do the denominator calculation ")


from CEN_FUNC_FILE import num_lag_calc
empty_array_num=num_lag_calc(matrix, rows, cols)


print("Now finding the values for the denominator  ")


from CEN_FUNC_FILE import den_lag_calc
empty_array_num=den_lag_calc(matrix, rows, cols,x_values, y_values, empty_array_num)



from CEN_FUNC_FILE import tot_sum
sum1=tot_sum(rows, cols,x_values, y_values, empty_array_num)        

# Create a lambda function from the sympy equation
x= sp.symbols('x')
equation_func = sp.lambdify(x, sum1, 'numpy')
   
# Generate x values
x_vals = np.linspace(-10, 10, 100)

# Evaluate the equation for the x values
y_vals = equation_func(x_vals)

# Create the plot
plt.plot(x_vals, y_vals)
plt.scatter(x_values, y_values)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of the equation')

# Show the plot
plt.show()      
        
        
        
        