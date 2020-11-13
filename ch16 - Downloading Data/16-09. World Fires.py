"""
Make a map that shows which parts of the world are affected by fires.
"""

import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Get data from 100000 places.
num_rows = 10_000

# Read data from CSV file.
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    # Create a reader object associated with that file.
    reader = csv.reader(f)
    # Return the next line in the file to get headers.
    header_row = next(reader)

    # Get brightnesses, lats and lons, and dates.
    dates, brightnesses = [], []
    lats, lons = [], []
    hover_texts = []
    row_num = 0
    for row in reader:
        # Convert the string to an object representing date.
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        # Convert the string to an object representing date.
        label = f"{date.strftime('%m/%d/%y')} - {brightness}"

        dates.append(date)
        brightnesses.append(brightness)
        lats.append(row[0])
        lons.append(row[1])
        hover_texts.append(label)

        row_num += 1
        if row_num == num_rows:
            break

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='Global Fire Activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
