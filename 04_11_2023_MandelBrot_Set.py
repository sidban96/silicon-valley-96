import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n

def plot_mandelbrot(c_real_range, c_imag_range, resolution, max_iter):
    x = np.linspace(c_real_range[0], c_real_range[1], resolution)
    y = np.linspace(c_imag_range[0], c_imag_range[1], resolution)

    mandelbrot_set = np.zeros((resolution, resolution), dtype=int)

    for i in range(resolution):
        for j in range(resolution):
            c = complex(x[i], y[j])
            mandelbrot_set[i, j] = mandelbrot(c, max_iter)

    plt.imshow(mandelbrot_set.T, extent=[c_real_range[0], c_real_range[1], c_imag_range[0], c_imag_range[1]])
    plt.colorbar()
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.title("Mandelbrot Set with Variable c")
    plt.show()

if __name__ == "__main__":
    c_real_range = (-2, 2)  # Real part of c range
    c_imag_range = (-2,2)  # Imaginary part of c range
    resolution = 500  # Resolution of the plot
    max_iter = 100  # Maximum number of iterations

    plot_mandelbrot(c_real_range, c_imag_range, resolution, max_iter)
