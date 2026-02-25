from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
import floodsystem.station
import floodsystem.plot

def main():
    datetoday = datetime.now()
    stations = build_station_list()
    for station in stations[:5]:
        floodsystem.plot.plot_water_levels(station, [datetoday-i for i in range(10, 0, -1)])


if __name__ == "__main__":
    main()