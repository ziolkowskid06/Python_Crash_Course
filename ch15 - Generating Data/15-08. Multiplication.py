"""
Roll two dice 1000000 times and multiply the results. Plot a histogram.
"""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000_001):
    # Multiply two numbers.
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# Set axes parameters.
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
# Set a layout and configuration of the graph as the whole.
my_layout = Layout(title='Results of multiplying two D6 dice. (1,000,000 rolls)',
                   xaxis=x_axis_config, yaxis=y_axis_config)

# Generate the plot and save in html file.
offline.plot({'data': data, 'layout': my_layout}, filename='d6d6.html')
