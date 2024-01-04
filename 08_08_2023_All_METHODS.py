import numpy as np
import matplotlib.pyplot as plt

start = -50
stop = 50
interval = 0.01
x_values = np.arange(start, stop, interval)
print(len(x_values))
mean = np.mean(x_values)
squared_diff = np.square(x_values - mean)
sample_std_dev = np.sqrt(np.sum(squared_diff) / ((stop-start/interval) - 1))

print("Sample Standard Deviation:", sample_std_dev)

y_values = np.exp(-x_values**2 / (2 * sample_std_dev**2))

plt.plot(x_values, y_values)


from CEN_FUNC_FILE import trap
area_trap=trap(x_values, y_values)


from CEN_FUNC_FILE import simp_1_3
area_simp_1_3=simp_1_3(x_values, y_values, start, stop)


from CEN_FUNC_FILE import composite_simpson_1_3
area_composite_simp_1_3=composite_simpson_1_3(x_values, y_values)
print(area_composite_simp_1_3)


from CEN_FUNC_FILE import simp_3_8
area_simp_3_8=simp_3_8(x_values, y_values, start, stop)