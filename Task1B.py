import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def main():
    answer_List = []
    stations = build_station_list()
    stationsByDistanceList = geo.stations_by_distance(stations, (52.2053, 0.1218))
    for stationAnswer in stationsByDistanceList:
        answer_List.append((stationAnswer[0].name, stationAnswer[0].town, stationAnswer[1]))
    print("The ten closest stations to the Cambridge city centre is", answer_List[:10])
    print("The ten farthest stations to the Cambridge city centre is", answer_List[-10:])

if __name__ == "__main__":
    main()