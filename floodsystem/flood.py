from collections import OrderedDict
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)
def stations_highest_rel_level(stations, N):
    """ This function returns the stations with the N highest relative water
    levels."""
    relative_water_level = []
    # Create dictionary of relevant stations with relative water levels
    for station in stations:
        if type(station.relative_water_level()) != float:
            continue
        else:
            relative_water_level.append((station.name, station.relative_water_level()))

    # Order dictionary by water heights
    relative_water_level.sort(key=lambda tup: tup[1], reverse = True)

    return relative_water_level[:N]
