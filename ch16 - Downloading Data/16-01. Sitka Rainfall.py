"""
Make a visualization focusing on the data in the column called PRCP,
which represents daily rainfall amounts.
"""

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Read data from CSV file.
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    # Create a reader object associated with that file.
    reader = csv.reader(f)
    # Return the next line in the file to get headers.
    header_row = next(reader)

    # Get date and rainfall amounts from this file.
    dates, precips = [], []
    for row in reader:
        # Convert the string to an object representing date.
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        precip = float(row[3])
        precips.append(precip)

# Plot the rainfall amounts.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue')

# Format plot.
plt.title("Daily Rainfall Amounts - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
# Draw date labels diagonally to prevent them overlapping.
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Show the plot.
plt.show()
