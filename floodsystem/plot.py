import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import matplotlib
import numpy as np


def plot_water_levels(station, dates, levels):
    # Plot
    low_range=[station.typical_range[0]]*(len(levels))
    high_range=[station.typical_range[1]]*(len(levels))
    plt.plot(dates, levels)
    plt.plot(dates, low_range)
    plt.plot(dates, high_range)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    poli=polyfit(dates, levels, p)
    plt.plot(dates, levels)
    x1 = np.linspace(x[0], x[-1], len(dates))
    plt.plot(dates, poli(x1))

    low_range=[station.typical_range[0]]*(len(levels))
    high_range=[station.typical_range[1]]*(len(levels))

    plt.plot(dates, low_range)
    plt.plot(dates, high_range)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
