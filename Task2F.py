from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime

stations = build_station_list()
update_water_levels(stations)

names = stations_highest_rel_level(stations, 5)
print (names)
list_names=[]
for name in names:
    list_names.append(name[0])
print (list_names)
#list_names.remove("Bampton Grange")

for station in stations:
        if station.name in list_names:
            dt = 2
            dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
            if len(dates)==0:
                print ("NO AVAILABLE DATA for:", station.name)
            else:
                plot_water_level_with_fit(station, dates, levels, 4)
