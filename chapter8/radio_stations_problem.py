
states_to_cover = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}

final_stations = set()

while states_to_cover:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_to_cover & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)
    states_to_cover -= states_covered


assert final_stations == {'kone', 'ktwo', 'kthree', 'kfive'}
