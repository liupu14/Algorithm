provinces_need = set(['guangdong', 'guangxi', 'yunnan', 'guizhou',
                      'fujian', 'zhejiang', 'hainan', 'hunan', 'jiangsu'])
Stations = {}
Stations['mongo'] = set(['hunan', 'jiangsu', 'guangdong'])
Stations['potato'] = set(['jiangsu', 'guizhou', 'yunnan', 'guangxi'])
Stations['waterbloon'] = set(
    ['guangdong', 'guangxi', 'zhejiang', 'jiangsu', 'fujian', 'hainan'])
final_stations = set()
while provinces_need:
    best_station = None
    station_covered = set()
    for station, station_for_province in Stations.items():
        covered = provinces_need & station_for_province
        if len(covered) > len(station_covered):
            best_station = station
            station_covered = covered
    provinces_need -= station_covered
    final_stations.add(best_station)
