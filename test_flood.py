from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():
    s1 = MonitoringStation("station_1", "measure_id", "station_1",
                                     (-2.0, 4.0), (0.0, 1.0), "river", "town")
    s2 = MonitoringStation("station_2", "measure_id", "station_2",
                                     (-2.0, 4.0), (0.0, 1.0), "river", "town")
    s3 = MonitoringStation("station_3", "measure_id", "station_3",
                                     (-2.0, 4.0), (0.0, 1.0), "river", "town")
    s4 = MonitoringStation("station_4", "measure_id", "station_4",
                                     (-2.0, 4.0), (0.0, 1.0), "river", "town")

    s1.latest_level = 3.0
    s2.latest_level = 1.0
    s3.latest_level = 4.0
    s4.latest_level = 2.0

    stations = [s1, s2, s3, s4]

    stations_at_risk = stations_highest_rel_level(stations, 4)

    assert stations_at_risk == [('station_3', 4.0), ('station_1', 3.0), ('station_4', 2.0), ('station_2', 1.0)]
