from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    top5 = stations_highest_rel_level(stations, 5)  # list of (station, level) tuples

    for station, _ in top5:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=10)
        )
        if dates and levels:
            plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    run()