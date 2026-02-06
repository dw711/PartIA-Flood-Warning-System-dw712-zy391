from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo


def main():
    stations = build_station_list()

    rivers_with_station = geo.rivers_with_station(stations)
    print(rivers_with_station[:10])

    geo.stations_by_river(())
