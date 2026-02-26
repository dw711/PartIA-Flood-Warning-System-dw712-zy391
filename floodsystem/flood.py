def stations_level_over_threshold(stations, tol):

    result = []

    for station in stations:
        rel_level = station.relative_water_level()

        if rel_level is not None and rel_level > tol:
            result.append((station, rel_level))

    result.sort(key=lambda x: x[1], reverse=True)

    return result


def stations_highest_rel_level(stations, N):
    list_of_highest_water_levels = []
    N_highest_water_levels = []
    for station in stations:
        rel_level = station.relative_water_level()
        if rel_level is not None:
            list_of_highest_water_levels.append((station, rel_level))
    list_of_highest_water_levels.sort(key=lambda x: x[1], reverse=True)
    for i in range(N):
        N_highest_water_levels.append(list_of_highest_water_levels[i])

    return N_highest_water_levels


    