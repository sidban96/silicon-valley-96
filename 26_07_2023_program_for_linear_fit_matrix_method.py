import numpy as np
import matplotlib.pyplot as plt
import sympy as sp



x = np.array([1, 2, 3, 9, 5])

y = np.sin(x)


from CEN_FUNC_FILE import sum_xi
sum_xi_1=sum_xi(x)

from CEN_FUNC_FILE import sum_xi2
sum_xi2_1=sum_xi2(x)

from CEN_FUNC_FILE import sum_yi
sum_yi_1=sum_yi(y)

from CEN_FUNC_FILE import sum_xi_yi
sum_xi_yi_1=sum_xi_yi(x,y)
    

from CEN_FUNC_FILE import solver
sol=solver(x,sum_xi_1,sum_xi2_1,sum_yi_1,sum_xi_yi_1)
# Print the solution
print("Solution:", sol)

               