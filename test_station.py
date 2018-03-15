"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations



def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    
    s1 = MonitoringStation("station_1", "measure_id", "station_1", 
                                     (-2.0, 4.0), None, "river", "town")
    s2 = MonitoringStation("station_2", "measure_id", "station_2", 
                                     (-2.0, 4.0), (0.432, 3.23), "river", "town")    
    s3 = MonitoringStation("station_3", "measure_id", "station_3", 
                                     (-2.0, 4.0), (0.432, 2.43), "river", "town")
    s4 = MonitoringStation("station_4", "measure_id", "station_4", 
                                     (-2.0, 4.0), (4.432, 3.43), "river", "town")    

    stations = [s1, s2, s3, s4]

    assert inconsistent_typical_range_stations(stations) == ["station_1", "station_4"]


def test_relative_water_level():
    
    s1 = MonitoringStation("station_1", "measure_id", "station_1", 
                                     (-2.0, 4.0), None, "river", "town")
    s2 = MonitoringStation("station_2", "measure_id", "station_2", 
                                     (-2.0, 4.0), (1.0, 2.0), "river", "town")
    s3 = MonitoringStation("station_3", "measure_id", "station_3", 
                                     (-2.0, 4.0), (1.0, 2.0), "river", "town")
    s1.latest_level = None
    s2.latest_level = 1.0
    s3.latest_level = 4.0
    
    #print(s2.typical_range)
    #print(s2.relative_water_level())
    
    assert s1.relative_water_level() == None
    assert s2.relative_water_level() == 0
    assert s3.relative_water_level() == 3
