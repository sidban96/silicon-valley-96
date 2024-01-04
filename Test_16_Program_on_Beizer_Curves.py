import os
import numpy as np
import matplotlib.pyplot as plt

os.system('cls')

poly_x_1=[]
poly_y_1=[]

n= int(input("Enter the number of polynomials"))

#filling up the arrays with the data points 
#filling up the x and y points 

for i in range(n):
 print("X"+str(i+1))
 poly_x=float(input("Enter the x value"))
 poly_x_1.append(poly_x)
 print("Y"+str(i+1))
 poly_y=float(input("Enter the y value"))
 poly_y_1.append(poly_y)
print(poly_x_1)

print(poly_y_1)

# Plot the data
plt.scatter(poly_x_1,poly_y_1, label='x and y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('x and y')

# Add legend
plt.legend()

# Show the plot
plt.show()


t= float(input("Enter the ratio  t for Beizer Curves"))

def P(x,len,ratio):
    result=[]
    for i in range(len):
        result.append( (1-ratio)*x[i] +(ratio)*x[i])
    return result

Points_x=[]
Points_y=[]

for i in range(n):
    Points_x=P(poly_x_1,n,t)
    print(Points_x)
    Points_y=P(poly_y_1,n,t)
    print(Points_y)