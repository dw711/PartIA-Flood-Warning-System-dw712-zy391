from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def main():
    # Build list of stations
    stations = build_station_list()

    # Update latest water levels
    update_water_levels(stations)

    # Get stations where relative level > 0.8
    stations_over = stations_level_over_threshold(stations, 0.8)

    # Print results
    for station, rel_level in stations_over:
        print(station.name, rel_level)


if __name__ == "__main__":
    main()