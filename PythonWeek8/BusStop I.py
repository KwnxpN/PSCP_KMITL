"""KKKK"""

def bus_stop(passengers, stop):
    """Count the passengers that get to desired stop"""
    passengers_now, all_stop = [], []
    passengers_count = 0
    for _ in range(stop):
        get_stop = str(input()).split()
        get_stop = list(map(int, get_stop))
        all_stop.append([get_stop[0], get_stop[1:]])
    all_stop.sort()
    for stop_now in all_stop:
        if stop_now[0] in passengers_now:
            for _ in range(passengers_now.count(stop_now[0])):
                passengers_now.remove(stop_now[0])
                passengers_count += 1
        for people in stop_now[1]:
            bus_size = len(passengers_now)
            if bus_size < passengers and people > stop_now[0]:
                passengers_now.append(people)
            elif bus_size >= passengers:
                break
    print(passengers_count)
bus_stop(int(input()), int(input()))
