from floodsystem.geo import stations_by_distance   
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    stations_sorted = stations_by_distance((52.2053, 0.1218))
    assert stations_sorted[0]==('Cambridge Jesus Lock', 0.8402364350834995)
    assert stations_sorted[-1]==('Penberth', 467.53367291629183)

def test_build_river_list():
    stations = build_station_list()
    rivers=(rivers_with_station(stations))
    assert len(set(rivers))==844

def test_dictionary_build():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    rivertest ={}
    rivertest.setdefault(s.river,[]).append(s.name)
    assert rivertest["River X"]==['some station']

def test_stations_radius():
    stations = build_station_list()
    a=stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert a[0]=='Bin Brook'
    assert len(a)==11
