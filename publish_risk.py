"""Write the current flood-risk assessment to site/risk.json.

Runs the Task 2G assessment (relative water level, plus whether the river is
rising) over every active station, keeps the worst risk per town, and saves a
small JSON summary that duowang.dev reads. A scheduled GitHub Action runs this
every 30 minutes and publishes site/ with GitHub Pages.

    python publish_risk.py [output_path]
"""

import datetime
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor

import requests

from floodsystem import datafetcher
from floodsystem.stationdata import build_station_list, update_water_levels
from Task2G import risk_level

WORKERS = 8
TIMEOUT_SECONDS = 20


def _fetch_with_timeout(url):
    """Same as datafetcher.fetch, but a slow request can't hang the whole run."""
    r = requests.get(url, timeout=TIMEOUT_SECONDS)
    r.raise_for_status()
    return r.json()


datafetcher.fetch = _fetch_with_timeout

ORDER = {"Low": 1, "Moderate": 2, "High": 3, "Severe": 4}
SOURCE = ("Environment Agency flood and river level data from the real-time data API (Beta). "
          "Contains public sector information licensed under the Open Government Licence v3.0.")


def assess():
    stations = build_station_list(use_cache=False)
    update_water_levels(stations)

    candidates = [
        s for s in stations
        if s.town and s.relative_water_level() is not None and s.relative_water_level() >= 1
    ]

    def assess_one(station):
        try:
            return station, risk_level(station)
        except Exception as exc:  # one bad station must not stop the run
            print(f"skipped {station.name}: {exc}", file=sys.stderr)
            return station, None

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(assess_one, candidates))

    towns = {}  # town -> (risk, relative level, river)
    checked = 0
    for station, risk in results:
        if risk is None:
            continue
        rel = station.relative_water_level()
        checked += 1
        best = towns.get(station.town)
        if best is None or (ORDER[risk], rel) > (ORDER[best[0]], best[1]):
            towns[station.town] = (risk, rel, station.river)

    ranked = sorted(towns.items(), key=lambda kv: (ORDER[kv[1][0]], kv[1][1]), reverse=True)
    counts = {level.lower(): 0 for level in ORDER}
    for _, (risk, _, _) in ranked:
        counts[risk.lower()] += 1

    return {
        "note": "Estimate from this project's own model, not official Environment Agency flood warnings.",
        "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "stations_total": len(stations),
        "stations_above_typical": len(candidates),
        "stations_assessed": checked,
        "counts": counts,
        "top": [
            {"town": town, "risk": risk, "river": river, "relative_level": round(rel, 2)}
            for town, (risk, rel, river) in ranked
            if risk in ("Severe", "High")
        ][:10],
        "source": SOURCE,
    }


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join("site", "risk.json")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    result = assess()
    with open(out, "w") as f:
        json.dump(result, f, indent=1)
    print(json.dumps(result["counts"]), "->", out)


if __name__ == "__main__":
    main()
