from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def main():
    stations = build_station_list()
    bad_stations = inconsistent_typical_range_stations(stations)
    names = sorted([station.name for station in bad_stations])
    print(names)

if __name__ == "__main__":
    main()