# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import numpy

def stations_by_distance(stations: list, p: tuple) -> list:
    answerList = []
    for station in stations:
        station_latitude, station_longitude = numpy.radians(station.coord)

        coord_latitude, coord_longitude = numpy.radians(p)
        #taking latitudes and longitudes for harvesine formula
        delta_lat = coord_latitude - station_latitude
        delta_long = coord_longitude - station_longitude

        hav_theta = (numpy.sin(delta_lat/2))**2 + numpy.cos(coord_latitude)*numpy.cos(station_latitude)*((numpy.sin(delta_long/2))**2)
        theta = 2*numpy.arcsin(numpy.sqrt(hav_theta))
        distance = 6371 * theta

        answerTuple = (station, distance)
        answerList.append(answerTuple)
    return sorted_by_key(answerList, 1)

def stations_within_radius(stations: list, x:tuple, radius:float) -> list:
    stationsByDistanceList = stations_by_distance(stations, x)
    stations_within_radius_list = []
    for stationTuple in stationsByDistanceList:
        if stationTuple[1] < radius:
            stations_within_radius_list.append(stationTuple[0])
        else:
            break
    return stations_within_radius_list

def rivers_with_station(stations: list) -> set:
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations: list) -> dict:
    rivers = rivers_with_station(stations)
    mapping = {}
    for river in rivers:
        station_in_river = []
        for station in stations:
            if station.river == river:
                station_in_river.append(station)
        mapping[river] = station_in_river
    return mapping