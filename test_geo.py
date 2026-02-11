import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

#testing stations by distance

def test_stations_by_distance():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    results = geo.stations_by_distance(stations, centre)
    assert isinstance(results, list) #ensurs output is list
    assert len(stations) == len(results) #testing that the length of list hasn't been altered

#Testing stations_within_radius:

def test_stations_within_radius():
    stations = build_station_list()
    sorted_stations = geo.stations_by_distance(stations, (52.2053, 0.1218))
    radius = 10
    result = geo.stations_within_radius(stations, (52.2053, 0.1218), radius)
    assert isinstance (result, list) #ensures output is a list
    assert result == sorted(result) #ensures output is sorted
    for i in range(len(result)):
        assert sorted_stations[i][1] < radius

#Testing rivers_by_station_number

def test_rivers_by_station_number():
    stations =  build_station_list()
    result = geo.rivers_by_station_number(stations, 9)
    assert isinstance(result, list) #ensures output is a list
    assert len(result) >=9 #ensures length is at least 9
    assert result == geo.sorted_by_key(result, 1, True) #ensures list is sorted correctly

#Testing stations_by_river

def test_stations_by_river():
    stations = build_station_list()
    result = geo.stations_by_river(stations)
    assert isinstance(result, dict) #ensures output is a dictionary
    rivers = geo.rivers_with_station(stations)
    assert len(result) == len(rivers) #ensures dictionary length is the same as that of the rivers