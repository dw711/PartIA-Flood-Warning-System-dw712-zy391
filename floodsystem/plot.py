import matplotlib.pyplot as plt
import matplotlib.dates as mpldates
import floodsystem.analysis

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)


    typical_range_list_low = [station.typical_range[0] for i in dates]
    typical_range_list_high = [station.typical_range[1] for i in dates]
    plt.plot(dates, typical_range_list_low)
    plt.plot(dates, typical_range_list_high)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station" + station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = floodsystem.analysis.polyfit(dates, levels, p)
    
    # Plot raw data
    plt.plot(dates, levels, label='water level')
    
    # Generate fit over shifted float x-values, then convert back to dates for plotting
    import numpy as np
    x = mpldates.date2num(dates)
    x_shifted = x - d0
    x_fit = np.linspace(x_shifted[0], x_shifted[-1], 100)
    dates_fit = mpldates.num2date(x_fit + d0)
    plt.plot(dates_fit, poly(x_fit), label=f'degree {p} fit')
    
    # Typical range lines (only if data is consistent)
    if station.typical_range_consistent():
        plt.axhline(y=station.typical_range[0], color='g', linestyle='--', label='typical low')
        plt.axhline(y=station.typical_range[1], color='r', linestyle='--', label='typical high')
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()
    plt.tight_layout()
    plt.show()