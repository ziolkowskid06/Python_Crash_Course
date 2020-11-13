"""
PLot daily high and low temperatures in Death Valley.
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Read data from CSV file.
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    # Create a reader object associated with that file.
    reader = csv.reader(f)
    # Return the next line in the file to get headers.
    header_row = next(reader)

    # Get dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        # Convert the string to an object representing date.
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # Detect if any data is missing.
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
# Set colors for both temperatures, and transparency. Fill the area between.
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=16)
# Draw date labels diagonally to prevent them overlapping.
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Show the plot.
plt.show()
