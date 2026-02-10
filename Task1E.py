from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo


def main():
    stations = build_station_list()

    rivers_by_number = geo.rivers_by_station_number(stations, 9)
    print(rivers_by_number)


if __name__ == "__main__":
    main()