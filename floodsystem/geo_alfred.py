"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key
from haversine import haversine

"""
This is Akil's code - Task 1C 
"""
def stations_within_radius(stations, centre, r):
    """
    This function takes a specified coordinate 'centre' and returns stations in 
    a specified radius, 'r' in km. 'Stations' is a list of tuples 
    (station_name, coordinates).
    """

    # Stations within the radius will be appended to this list
    stations_in_radius = []
    
    for station in stations:
        
        # Appends station if station-centre distance < r
        if haversine(centre, station.coord) < r:
            stations_in_radius.append(station.name)

    # Sort list alphabetically and print
    stations_in_radius.sort()
    print(stations_in_radius)
    
    # ?? Why can't you use .sort there

    return stations_in_radius

"""
This is Alfred's code - Task 1B and 1D
"""
"""This module contains a collection of functions related to
geographical data.

"""
from .stationdata import build_station_list


def stations_by_distance(p):
    distance = []
    stationname = []
    name_distance = []

    stations = build_station_list()
    for station in stations:
            stationname.append(station.name)
            distance.append(haversine(station.coord,p))
    i=0
    while i<len(stationname):
        name_distance.append((stationname[i],distance[i]))
        i+=1
    return sorted_by_key((name_distance),1)
    
def rivers_with_station(station_list):
    rivers =[]
    for station in station_list:
        rivers.append(station.river)
    return (set(rivers))
   
def stations_by_river():
    riverdic ={}
    stations = build_station_list()
    for station in stations:
        riverdic.setdefault(station.river,[]).append(station.name)
    return riverdic

"""
Task 1E - Akil
"""
import operator

def rivers_by_station_number(stations, N):
    """
    A function that determines the N rivers with the greatest number of 
    monitoring stations. 
    """
    riverdic = {};     riverdic_N = []      

    # Adds unique rivers to riverdic and assigns value for number of stations on river
    for station in stations:
        if station.river not in riverdic:
            riverdic[station.river] = 1
        else:
            riverdic[station.river] += 1

    # Creates ordered tuple list from dictionary. Descending by station frequency.
    sorted_riverdic = sorted(riverdic.items(), key=operator.itemgetter(1), reverse = True)
    
    # Creates list of stations with 'N' highest unique station frequency values
    n = 0; i = 0
    while n < N:
        if sorted_riverdic[i][1] == sorted_riverdic[i+1][1]:
            riverdic_N.append(sorted_riverdic[i])
            i +=1
        else:
            riverdic_N.append(sorted_riverdic[i])
            n += 1; i += 1
    
    print(len(riverdic_N), " stations returned"); print(riverdic_N)
    
    return riverdic_N
    
    #Debugging code :  print("Repeated value ", i, sorted_riverdic[i], "=", sorted_riverdic[i+1])
    #Debugging code :  print(i, sorted_riverdic[i])