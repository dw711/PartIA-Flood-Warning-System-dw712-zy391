from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def main():
    stations = build_station_list()
    update_water_levels(stations)

    top10 = stations_highest_rel_level(stations, 10)

    for station, level in top10:
        print(f"{station.name} {level}")

if __name__ == "__main__":
    main()