from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)

    top_5_stations = stations_highest_rel_level(stations, 5)

    for station in top_5_stations:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=2))
        if not dates or not levels:
            continue  # Skip if no data is available
        plot_water_level_with_fit(station[0], dates, levels, 4)

if __name__ == "__main__":
    run()