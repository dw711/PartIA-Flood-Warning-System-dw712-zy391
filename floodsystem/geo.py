# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import math

def stations_by_distance(stations: list, p: tuple) -> list:
    answerList = []
    for station in stations:
        station_latitude = math.radians(station.coord[0])
        station_longitude = math.radians(station.coord[1])

        coord_latitude = math.radians(p[0])
        coord_longitude = math.radians(p[1])
        #taking latitudes and longitudes for harvesine formula
        delta_lat = coord_latitude - station_latitude
        delta_long = coord_longitude - station_longitude

        hav_theta = (math.sin(delta_lat/2))**2 + math.cos(coord_latitude)*math.cos(station_latitude)*((math.sin(delta_long/2))**2)
        theta = 2*math.asin(math.sqrt(hav_theta))

        assert hav_theta <= 1
        distance = 6371 * theta

        answerTuple = (station, distance)
        answerList.append(answerTuple)
    return sorted_by_key(answerList, 1)