def number(bus_stops):
    Count = []
    for i in bus_stops:
        Count.append(i[0]-i[1])
    return sum(Count)
