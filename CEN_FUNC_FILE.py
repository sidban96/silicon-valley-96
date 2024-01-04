import os
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#Definitions for 25.07.2023

def q1(x_values, e1,e2):
    y= np.tanh(x_values/e1) + np.tanh(x_values/e2)
    return y

def q2(x_values, a1,a2, k1, k2):
    y= a1*np.sin(k1*x_values) + a2*np.cos(k2*x_values)
    return y


def q3(r,k,A,B,deg1,deg2,a,b):
    A_part= np.exp(-k * r) / r + np.exp(-k * a) / a + np.exp(-k * b) / b
    y = A * A_part + B * r ** 2
    return y











#Definitions for 25.07.2023

def sum_xi(x):
    # Summation of all the x(i)
    sum_xi=0
    for i in range(len(x)):
        sum_xi+=x[i]
    
    return sum_xi

def sum_xi2(x):
    # Summation of all the x(i)^2
    sum_xi2=0
    for i in range(len(x)):
        sum_xi2+=x[i]**2
    return sum_xi2


def sum_yi(y):
    # Summation of all the y(i)
    sum_yi=0
    for i in range(len(y)):
        sum_yi+=y[i]
    return sum_yi

def sum_xi_yi(x,y):
    # Summation of all the x(i) * y(i)
    mul_xi_yi=1
    sum_xi_yi=0
    for i in range(len(x)):
        mul_xi_yi=x[i]*y[i]
        sum_xi_yi+=mul_xi_yi
    
    return sum_xi_yi

def solver(x,sum_xi_1,sum_xi2_1,sum_yi_1,sum_xi_yi_1):
    # Now we solve the equations for the slope m and constant c
    m, c = sp.symbols('m c')

    # Define the equations
    equation1 = sp.Eq(sum_xi2_1*m - sum_xi_1*c, sum_xi_yi_1)
    equation2 = sp.Eq(sum_xi_1*m - len(x)*c, sum_yi_1)

    # Solve the system of equations
    solution = sp.solve((equation1, equation2), (m, c))
    return solution




















        
# Definition for 01.08.2023 Lagrange Interpolation

def mat_inp(n,x_values,rows,cols): 
    x= sp.symbols('x')
    


    print("Initialize an empty matrix")
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]


    # Fill the matrix using a for loop
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] =(x-x_values[j])

    # Print the resulting matrix
    for row in matrix:
        print(row)
        
    return matrix

def num_lag_calc(matrix, rows, cols ):
    empty_array_num=[[1 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if i==j:
                print("Skip")
                print(i,j)
                continue
            else:
                empty_array_num[i][0]*=matrix[i][j]
    # Print the resulting matrix
    for row in empty_array_num:
        print(row)   

    return  empty_array_num





def den_lag_calc(matrix, rows, cols,x_values, y_values, empty_array_num):
    
    # Initialize an empty matrix
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    empty_array_den=[[1 for _ in range(cols)] for _ in range(rows)]
    # Fill the matrix using a for loop
    for i in range(rows):
        for j in range(cols):
            if i==j:
                print("Skip")
                print(i,j)
                continue
            else:
                matrix[i][j] =(x_values[i]-x_values[j])
                empty_array_den[i][0]*=matrix[i][j]
                empty_array_den[i][0]=y_values[i]*empty_array_den[i][0]
                empty_array_num[i][0]=empty_array_num[i][0]*empty_array_den[i][0]
     

    # Print the resulting matrix
    for row in empty_array_num:
        print(row)
    return empty_array_num





def tot_sum(rows, cols,x_values, y_values, empty_array_num):
    sum1=0
    for i in range(rows):
        for j in range(cols):
            if empty_array_num[i][j]==1:
                print("Not Required")
                continue
            else:
                sum1+=empty_array_num[i][j]


    print(sum1)
    return sum1
        
 
    
    
# definitions for 08.08.2023


def trap(x_values,y_values):
    print("To find out the area using trapezoidal method")
    sum=0.00

    for i in range(len(y_values)-1):
         sum+=0.5*(x_values[i+1]-x_values[i])*(y_values[i+1]+y_values[i])


    print(sum)
    return sum


def simp_1_3(x_values,y_values,start,stop):
    print("To find out the area using basic Simpson method")

    n=len(y_values)-1
    midpoint=(0+n)//2

    area=((stop-start)/6)*(y_values[0]+y_values[n]+4*y_values[midpoint])

    print(area)
    return area

def composite_simpson_1_3(x_values, y_values):
    print("To find out the area using Composite Simpson method")
    h = x_values[1] - x_values[0]
    n = len(x_values) - 1
    area = y_values[0] + y_values[n]

    for i in range(1, n, 2):
        area += 4 * y_values[i]

    for i in range(2, n - 1, 2):
        area += 2 * y_values[i]
    
    return (h / 3) * area

def simp_3_8(x_values,y_values,start,stop):
    print("To find out the area using Simpson 3/8 method")

    n=len(y_values)-1
    midpoint_1=(2*0+n)//3
    midpoint_2=(0+2*n)//3
    area=((stop-start)/8)*(y_values[0]+y_values[n]+3*y_values[midpoint_1]+3*y_values[midpoint_2])

    print(area)
    return area


    