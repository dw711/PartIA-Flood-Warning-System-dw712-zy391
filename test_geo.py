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
    print(sorted_stations[0][1])
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

#Testing rivers_with_station

def test_rivers_with_station():
    """Test extraction of unique river names from stations"""
    from floodsystem.station import MonitoringStation
    
    # Test with multiple stations on same river
    s1 = MonitoringStation("id1", "m1", "A", (0, 0), (1, 5), "River Thames", "Town1")
    s2 = MonitoringStation("id2", "m2", "B", (0, 0), (1, 5), "River Thames", "Town2")
    s3 = MonitoringStation("id3", "m3", "C", (0, 0), (1, 5), "River Cam", "Town3")
    
    stations = [s1, s2, s3]
    result = geo.rivers_with_station(stations)
    
    assert isinstance(result, set)
    assert len(result) == 2
    assert "River Thames" in result
    assert "River Cam" in result
    
    # Test with single river
    single_river_stations = [s1, s2]
    result_single = geo.rivers_with_station(single_river_stations)
    assert len(result_single) == 1
    assert "River Thames" in result_single
    
    # Test with empty list
    result_empty = geo.rivers_with_station([])
    assert isinstance(result_empty, set)
    assert len(result_empty) == 0