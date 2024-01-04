import random
import matplotlib.pyplot as plt
INTERVAL = 1000
cle_points=0
circle_points = 0
square_points = 0
x=[]
y=[]
# Total Random numbers generated= possible x
# values* possible y values
for i in range(INTERVAL**2):

 rand_x = random.uniform(-1, 1)
 x.append(rand_x)
 rand_y = random.uniform(-1, 1)
 y.append(rand_y)
	# Distance between (x, y) from the origin
 origin_dist = rand_x**2 + rand_y**2

	# Checking if (x, y) lies inside the circle
 if origin_dist <= 1:
     cle_points += 1

 square_points += 1

	# Estimating value of pi,
	# pi= 4*(no. of points generated inside the
	# circle)/ (no. of points generated inside the square)
 pi = 4 * circle_points / square_points

## print(rand_x, rand_y, circle_points, square_points, "-", pi)
# print("\n")
plt.plot(rand_x,rand_y)
#plt.title('Sine Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

print("Final Estimation of Pi=", pi)
