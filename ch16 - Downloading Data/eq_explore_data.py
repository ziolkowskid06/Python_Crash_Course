"""
Render a map of earthquakes, showing their coordinates. 
"""

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    # Convert data into format Python.
    all_eq_data = json.load(f)

# Write same data into a more readable format.
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    # Take JSON data object and a file object and write data to that file.
    # Format the data using indentation that matches the data's structure.
    json.dump(all_eq_data, f, indent=4)

# Create an object to see information about each place.
all_eq_dicts = all_eq_data['features']

# Store data from every earthquake.
mags, lons, lats = [], [], []
for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the eqrthquakes.
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
