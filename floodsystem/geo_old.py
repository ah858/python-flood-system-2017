"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from haversine import haversine

"""
This is Akil's code - Task 1C - RECOPIED IN TASK C FILE
"""

def stations_within_radius(stations, centre, r):
    """
    This function takes a specified coordinate 'centre' and returns stations in 
    a specified radius, 'r' in km. 'Stations' is a list of tuples 
    (station_name, coordinates).
    """

    #   Stations within the radius will be appended to this list
    stations_in_radius = ()
    
    for station in stations:
        
        # Appends station if station-centre distance > r
        if distance = haversine(centre, station[1]) > r:
        append.stations_in_radius(station[0])
        
    print stations_in_radius

return stations_in_radius