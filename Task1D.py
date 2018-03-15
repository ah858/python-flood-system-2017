from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
stations = build_station_list()
list_of_all_rivers=sorted(rivers_with_station(stations))
print (len(list_of_all_rivers))
print (list_of_all_rivers[0:10])

dic_of_rivers=stations_by_river()


riv = str(input("What is the river?"))
print (sorted(dic_of_rivers[riv]))

"River Aire, River Cam, Thames"
