from floodsystem.geo import stations_by_distance 
stations_sorted = stations_by_distance((52.2053, 0.1218))
ten_closest=stations_sorted[0:10]
ten_furthest=stations_sorted[-10:]
print(ten_closest+ten_furthest)
