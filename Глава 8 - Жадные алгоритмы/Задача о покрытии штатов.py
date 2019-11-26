states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"} # Все доступные штаты

stations = dict() # Объявление радиостанций и штатов, на которых они играют
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}

final_stations = set() # Нам требуется покрыть все штаты, выбрав как можно меньше радиостанций

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states  # Находим еще непокрытые штаты
        if len(covered) > len(states_covered):  # Если этот набор больше уже выбранного наилучшего
            best_station = station
            states_covered = covered

    # Указываем, какие штаты покрыли
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)