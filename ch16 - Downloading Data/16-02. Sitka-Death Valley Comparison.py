"""
Make  a direct comparison between temperature rages in Sitka and Death Valley.
You need identical scales on the y-axis.
"""

import csv
from datetime import datetime

from matplotlib import pyplot as plt


def get_weather_data(filename, dates, highs, lows, date_index, high_index,
                     low_index):
    """Get the highs and lows from a data file."""
    with open(filename) as f:
        # Create a reader object associated with that file.
        reader = csv.reader(f)
        # Return the next line in the file to get headers.
        header_row = next(reader)

        # Get date, and high and low temperatures form this file.
        for row in reader:
            # Convert the string to an object representing date.
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            # Detect if any data is missing.
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


# Get weather data for Sitka.
filename = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=5,
                 low_index=6)

# Plot Sitka weather data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
# Set colors for both temperatures, and transparency. Fill the area between.
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Get weather data for Death Valley.
filename = 'data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=4,
                 low_index=5)

# Add Death Valley data to  current plot.
# Set colors for both temperatures, and transparency. Fill the area between.
ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)


# Format plot.
title = "Daily high and low temperatures - 2018"
title += "\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
# Draw date labels diagonally to prevent them overlapping.
fig.autofmt_xdate()
plt.ylabel("Tmeperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

# Show the plot.
plt.show()
