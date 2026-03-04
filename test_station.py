# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

from floodsystem.station import MonitoringStation

def test_typical_range_consistent():

    # Range okay
    s1 = MonitoringStation("id1", "m1", "A", (0,0), (1, 5), "River", "Town")
    assert s1.typical_range_consistent() == True

    # None range
    s2 = MonitoringStation("id2", "m2", "B", (0,0), None, "River", "Town")
    assert s2.typical_range_consistent() == False

    # High < Low should give false
    s3 = MonitoringStation("id3", "m3", "C", (0,0), (5, 1), "River", "Town")
    assert s3.typical_range_consistent() == False

from floodsystem.station import inconsistent_typical_range_stations

def test_inconsistent_typical_range_stations():
#valid 
    s1 = MonitoringStation("id1", "m1", "A", (0,0), (1, 5), "River", "Town")
    #none
    s2 = MonitoringStation("id2", "m2", "B", (0,0), None, "River", "Town")
    #high<low should be in result
    s3 = MonitoringStation("id3", "m3", "C", (0,0), (5, 1), "River", "Town")

    stations = [s1, s2, s3]

    result = inconsistent_typical_range_stations(stations)

    assert s2 in result
    assert s3 in result
    assert s1 not in result

def test_relative_water_level():
    """Test relative water level calculation"""
    
    # Normal case: water level within range
    s1 = MonitoringStation("id1", "m1", "A", (0, 0), (1.0, 5.0), "River", "Town")
    s1.latest_level = 3.0
    assert s1.relative_water_level() == 0.5  # (3.0 - 1.0) / (5.0 - 1.0) = 0.5
    
    # Water level at low boundary
    s2 = MonitoringStation("id2", "m2", "B", (0, 0), (1.0, 5.0), "River", "Town")
    s2.latest_level = 1.0
    assert s2.relative_water_level() == 0.0
    
    # Water level at high boundary
    s3 = MonitoringStation("id3", "m3", "C", (0, 0), (1.0, 5.0), "River", "Town")
    s3.latest_level = 5.0
    assert s3.relative_water_level() == 1.0
    
    # Water level above range
    s4 = MonitoringStation("id4", "m4", "D", (0, 0), (1.0, 5.0), "River", "Town")
    s4.latest_level = 6.0
    assert s4.relative_water_level() == 1.25
    
    # Water level below range
    s5 = MonitoringStation("id5", "m5", "E", (0, 0), (1.0, 5.0), "River", "Town")
    s5.latest_level = 0.0
    assert s5.relative_water_level() == -0.25
    
    # No latest level data
    s6 = MonitoringStation("id6", "m6", "F", (0, 0), (1.0, 5.0), "River", "Town")
    s6.latest_level = None
    assert s6.relative_water_level() is None
    
    # Inconsistent typical range (high < low)
    s7 = MonitoringStation("id7", "m7", "G", (0, 0), (5.0, 1.0), "River", "Town")
    s7.latest_level = 3.0
    assert s7.relative_water_level() is None
    
    # None typical range
    s8 = MonitoringStation("id8", "m8", "H", (0, 0), None, "River", "Town")
    s8.latest_level = 3.0
    assert s8.relative_water_level() is None
