import os
import numpy as np
import matplotlib.pyplot as plt

os.system('cls')
"""

Now to write the equations one by one
1. y= tanh x/e1  +tanh x/e2 ; e1=0.1 and e2=0.01
2. y=a1 sin k1x + a2 cos k2x ; a1=1.0; a2=2.0; k1=2.0 ; k2=3.0
3. f(r)=A((e^(-kr)/r) + (e^(-ka)/a) + (e^(-kb)/b))+ B*r^2
A=1.0 B=1.0 k=0.1
a= 2*r*cos(54 deg)
b=4*r*cos(36 deg)*sin(54 deg)

"""

n=1

while n!=4:
    n=int(input("Choose the question to answer 1, 2 ,3 or Exit by typing 4-->  "))
    if n==1:
        e1=0.1
        e2=0.01
        x = np.arange(-5, 5, 0.01)
        # Import the add_numbers function from CEN_FUNC_FILE.py
        # to compute the given expression
        from CEN_FUNC_FILE import q1
        y=q1(x,e1,e2)
        # Plot the y function
        plt.plot(x, y, label='tanh(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('y= tanh x/e1  +tanh x/e2')
        plt.grid(True)
        # to show a specific part of the plot we will consider the following
        plt.xlim(-0.5,0.5)  
        plt.ylim(-2.5,2.5)

        plt.legend()
        plt.show()

    elif n==2: 
        a1=1.0 
        a2=2.0 
        k1=2.0 
        k2=3.0
        x = np.arange(-10, 10, 0.01)
        # Import the add_numbers function from CEN_FUNC_FILE.py
        # to compute the given expression
        from CEN_FUNC_FILE import q2
        y=q2(x,a1,a2,k1,k2)
        

        # Plot the y function
        plt.plot(x, y, label='y=a1 sin k1x + a2 cos k2x')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('y=a1 sin k1x + a2 cos k2x')
        plt.grid(True)


        # to show a specific part of the plot we will consider the following
        """plt.xlim(-0.5,0.5)
        plt.ylim(-2.5,2.5)"""

        plt.legend()
        plt.show()

    elif n==3:
        A = 1.0
        B = 1.0
        k = -0.1
        deg1 = (54)*(np.pi/180)
        deg2 = (36)*(np.pi/180)
        r = np.arange(-15, 15, 0.1)
        a = 2 * r * np.cos(deg1)
        b = 4 * r * np.cos(deg2) * np.sin(deg1)
        from CEN_FUNC_FILE import q3
        y=q3(r,k,A,B,deg1,deg2,a,b)
        

        # Plot the y function
        plt.plot(r, y, label='f(r)=A((e^(-kr)/r) + (e^(-ka)/a) + (e^(-kb)/b))+ B*r^2')
        plt.xlabel('r')
        plt.ylabel('y')
        plt.title('y=f(r)=A((e^(-kr)/r) + (e^(-ka)/a) + (e^(-kb)/b))+ B*r^2')
        plt.grid(True)
        plt.legend()
        plt.show()
    else:
        print("EXIT")
