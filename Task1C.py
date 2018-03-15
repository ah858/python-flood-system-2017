from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Ask user for input coordinates - suggested is for Cambridge
    centre_x = 52.2053 # input("Enter lattititude - eg. 52.2053 : ")
    centre_y = 0.1218  # input("Enter longitude - eg. 0.1218 : ")
    centre = (centre_x , centre_y)

    # Display stations in specified radius
    stations_within_radius(stations, centre, r = float(input("What is required radius? ")))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")

    # Run Task1C
    run()
