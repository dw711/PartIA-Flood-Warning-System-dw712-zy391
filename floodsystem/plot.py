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
    fixed_dates = mpldates.date2num(dates)-d0
    fittedy = poly(fixed_dates)
    plt.plot(fixed_dates, levels)
    plt.plot(fixed_dates, fittedy)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station" + station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()