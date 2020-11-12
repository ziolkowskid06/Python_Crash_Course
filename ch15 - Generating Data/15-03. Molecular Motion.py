"""
Modification of rw_visual.py
Simulation of path of a pollen grain on the surface of a drop of water.
Uses refactored module random_walk.py
"""

import matplotlib.pyplot as plt

from random_walk_refactoring import RandomWalk

# Keep makin new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Plot result
    plt.show()

    keep_runing = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
