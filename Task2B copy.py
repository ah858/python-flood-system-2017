from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Print stations with relative water levels >= 0.8
    for station in stations:

        if station.relative_water_level() == None:
#            print("[", station.name, ",", 'Invalid data', "]")
            continue
        elif station.relative_water_level() >= 0.8:

            print("[", station.name, ",", \
                    format(station.relative_water_level(), '.2f'), "]")
        else:
            continue
#            print("Relative level < 0.8m")


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()
