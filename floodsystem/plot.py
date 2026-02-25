import matplotlib.pyplot as plt



def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)


    typical_range_list_low = [station.typical_range[0] for i in dates]
    typical_range_list_high = [station.typical_range[1] for i in dates]
    plt.plot(dates, typical_range_list_low, color = '-r')
    plt.plot(dates, typical_range_list_high, color= '-g')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station" + station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
        