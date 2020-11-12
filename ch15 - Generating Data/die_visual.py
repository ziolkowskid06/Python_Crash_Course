"""
Roll a dice 1000 times and plot the frequency of results (bar chart).
"""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1001):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results, making histogram.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

# Set axes titles.
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
# Set a layout and configuration of the graph as the whole.
my_layout = Layout(title='Results of rolling on D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

# Generate the plot and save in html file.
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
