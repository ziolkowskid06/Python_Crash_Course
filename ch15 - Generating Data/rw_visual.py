"""
Visualize a random walk.
"""


import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    # Set a figure size in inches.
    fig, ax = plt.subplots(figsize=(15, 9))
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues,
               edgecolors='none', s=1)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    # Ask for another walk.
    keep_running = input("Make antoher walk? (y/n): ")
    if keep_running == 'n':
        break
