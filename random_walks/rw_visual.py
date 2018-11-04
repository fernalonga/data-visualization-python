import matplotlib.pyplot as plt 
from random_walk import RandomWalk 
# Make a random walk, and plot its points.
while True:
	# Create a random walk object and fill its points.
	rw = RandomWalk(50000)
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
	# Emphasize first and last points.
	plt.scatter(0, 0, c='green', edgecolors='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
	# Remove axes.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	# Show generated graphics
	plt.show()
	# Ask user about program re-execution.
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break