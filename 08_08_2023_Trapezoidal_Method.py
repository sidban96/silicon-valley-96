import numpy as np
import matplotlib.pyplot as plt

start = -50
stop = 50
interval = 0.1
x_values = np.arange(start, stop, interval)

mean = np.mean(x_values)
squared_diff = np.square(x_values - mean)
sample_std_dev = np.sqrt(np.sum(squared_diff) / ((stop-start/interval) - 1))

print("Sample Standard Deviation:", sample_std_dev)

y_values = np.exp(-x_values**2 / (2 * sample_std_dev**2))
print(y_values)
plt.plot(x_values, y_values)
print("Sample Standard Deviation:", sample_std_dev)
print("To find out our starting point for trapezoidal method")



sum=0.00

for i in range(len(y_values)-1):
     sum+=0.5*(x_values[i+1]-x_values[i])*(y_values[i+1]+y_values[i])


print(sum)
