from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo


def main():
    stations = build_station_list()

    rivers_with_station = [x for x in geo.rivers_with_station(stations)]
    rivers_with_station.sort()
    print(rivers_with_station[:10])
    

    river_to_stations_dict = geo.stations_by_river((stations))

    AireStations = [x.name for x in river_to_stations_dict["River Aire"]]
    AireStations.sort()
    print(AireStations)

    CamStations = [x.name for x in river_to_stations_dict["River Cam"]]
    CamStations.sort()
    print(CamStations)

    ThamesStations = [x.name for x in river_to_stations_dict["River Thames"]]
    ThamesStations.sort()
    print(ThamesStations)


if __name__ == "__main__":
    main()