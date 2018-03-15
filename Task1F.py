from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

"""Requirements for Task 1F"""

stations = build_station_list()
print(inconsistent_typical_range_stations(stations))

# DEBUGGING CODE
#for i in range(len(stations)):
#    if stations[i].typical_range_consistent() == False:
#        print(stations[i])
#        print("=======", i, "======")
