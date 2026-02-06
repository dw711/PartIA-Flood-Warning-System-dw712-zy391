import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def main():
    stations = build_station_list()

    stationList = geo.stations_within_radius(stations, (52.2053, 0.1218), 10.0)
    i=0
    for station in stationList:
        stationList[i] = station.name
        i += 1
    print(stationList)


if __name__ == "__main__":
    main()