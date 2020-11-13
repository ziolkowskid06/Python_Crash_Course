"""
Render a map of earthquakes, showinng their magnitude.
"""

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
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
mags, lons, lats, hover_texts = [], [], [], []
for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    title = eq_dicts['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the eqrthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
