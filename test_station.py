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
