"""
Create a scatter plot.
"""


import matplotlib.pyplot as plt

# X - values, and Y - values.
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Set a style and generate the plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
# Set a scatter plot, size and color of the points.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Save the plot. Trim extra whitespace around the plot.
plt.savefig('squares_plot.png', bbox_inches='tight')
