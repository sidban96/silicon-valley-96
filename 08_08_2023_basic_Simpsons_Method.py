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
print("To find out our starting point for basic Simpson method")

n=len(y_values)-1
midpoint=(0+n)//2

area=((stop-start)/6)*(y_values[0]+y_values[n]+4*y_values[midpoint])

print(area)



