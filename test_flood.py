from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():

    # Create fake stations
    s1 = MonitoringStation("id1", "m1", "A", (0,0), (0, 1), "River", "Town")
    s2 = MonitoringStation("id2", "m2", "B", (0,0), (0, 2), "River", "Town")
    s3 = MonitoringStation("id3", "m3", "C", (0,0), (0, 1), "River", "Town")

    # Fake latest levels
    s1.latest_level = 0.9  
    s2.latest_level = 1.0   
    s3.latest_level = None  # invalid

    stations = [s1, s2, s3]

    result = stations_level_over_threshold(stations, 0.6)

    # Only s1 should pass threshold 0.6
    assert len(result) == 1
    assert result[0][0] == s1
    assert result[0][1] == 0.9

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():

    # Create fake stations
    s1 = MonitoringStation("id1", "m1", "A", (0,0), (0, 1), "River", "Town")
    s2 = MonitoringStation("id2", "m2", "B", (0,0), (0, 1), "River", "Town")
    s3 = MonitoringStation("id3", "m3", "C", (0,0), (0, 1), "River", "Town")

    # fake latest levels
    s1.latest_level = 0.2   # relative = 0.2
    s2.latest_level = 0.9   # relative = 0.9
    s3.latest_level = 0.5   # relative = 0.5

    stations = [s1, s2, s3]

    result = stations_highest_rel_level(stations, 2)

    # Must return exactly 2 stations
    assert len(result) == 2

    # Should be sorted descending 
    assert result[0][0] == s2  # highest
    assert result[1][0] == s3  # second highest 

    # Ensure correct values returned
    assert result[0][1] == 0.9
    assert result[1][1] == 0.5