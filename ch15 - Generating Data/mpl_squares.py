"""
Create a plot by matching all points.
"""


import matplotlib.pyplot as plt

# X - values, and Y - values.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Set a style of the plot.
plt.style.use('seaborn-darkgrid')
# Generate one or more plots in the same figure, and adjuct the thickness.
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Squares Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Open Matplotlib's viewer and display the plot.
plt.show()
