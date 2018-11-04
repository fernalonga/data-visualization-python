import matplotlib.pyplot as plt

# Set axis-es values.
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Determine plot scattering.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greys, edgecolor='none', s=40)

# Set chart title and label axis.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value - 10^11", fontsize=14)

# Set axis-es range.
plt.axis([0, 5100, 0, 132651*(10**6)])

# Show graphs.
plt.show()