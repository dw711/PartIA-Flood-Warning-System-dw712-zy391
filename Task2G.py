from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np

def risk_level(station):
    """
    Criteria:
    - Base risk is determined by relative water level (fraction of typical range):
    >= 1.5 -> starts at High; < 1.0 -> starts at Low
    - If the water level is rising (avg of last 6 readings > avg of prior 6),
    the risk is escalated by one level. (i.e. from low to moderate, from high to severe)
    """
    rel_level = station.relative_water_level()
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
    if rel_level:
        if rel_level < 1.5:
            if np.average(levels[-6:]) > np.average(levels[-12:-6]): #i.e. the levels r rising
                return "Moderate"
            else:
                return "Low" #levels not rising, give low rating
        else:
            if np.average(levels[-6:]) > np.average(levels[-12:-6]): #i.e. the levels r rising
                return "Severe"
            else:
                return "High"

def run():
    stations = build_station_list()
    update_water_levels(stations)
    initial_at_risk_stations = []
    towns_at_risk = {}
    for station in stations:
        if station.relative_water_level():
            if station.relative_water_level() >= 1:
                initial_at_risk_stations.append(station)
    sort_dict = {"Low": 1, "Moderate": 2, "High": 3, "Severe": 4}
    for station in initial_at_risk_stations:
        risk = risk_level(station)
        if station.town in towns_at_risk:
            if sort_dict[risk] > sort_dict[towns_at_risk[station.town]]:
                towns_at_risk[station.town] = risk
        else:
            towns_at_risk[station.town] = risk
    return towns_at_risk

if __name__ == "__main__":
    print("Flood risk assessment by town")
    print("Criteria: relative water level thresholds (>= 1.5 = High/Severe, > 1.0 and < 1.5 = Low/Moderate)")
    print("decision between the two is from the trend of water levels. i.e. High/Moderate if it's rising, using the past 6 readings vs the 6 before that")
    towns = run()
    for town, risk in towns:
        print("The town:", town, "has risk:", risk)