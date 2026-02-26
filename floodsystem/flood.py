def stations_level_over_threshold(stations, tol):

    result = []

    for station in stations:
        rel_level = station.relative_water_level()

        if rel_level is not None and rel_level > tol:
            result.append((station, rel_level))

    result.sort(key=lambda x: x[1], reverse=True)

    return result