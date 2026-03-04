from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import numpy as np
import matplotlib.dates as mpldates

def risk_level(station):
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
    print(run())