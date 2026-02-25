from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
import floodsystem.datafetcher
import floodsystem.station
import floodsystem.plot

def main():
    datetoday = datetime.now()
    stations = build_station_list()
    for station in stations[:5]:
        dates, levels = floodsystem.datafetcher.fetch_measure_levels(station.measure_id, timedelta(10))
        floodsystem.plot.plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    main()