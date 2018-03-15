from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print station and latest level for first 5 stations in list
    stations_at_risk = stations_highest_rel_level(stations, 10)

    for station in stations_at_risk:
        print(station)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    run()
