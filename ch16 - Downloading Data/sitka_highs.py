"""
Plot daily high temperatures in Sitka.
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Read data from CSV file.
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    # Create a reader object associated with that file.
    reader = csv.reader(f)
    # Return the next line in the file to get headers.
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    # You can check headers indexes by calling enumerate method.
    for row in reader:
        # Convert the string to an object representing date.
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
# Draw date labels diagonally to prevent them overlapping.
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Show the plot.
plt.show()
