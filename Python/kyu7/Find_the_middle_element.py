def gimme(n):
    list = {n[0]: 0, n[1]: 1, n[2]: 2}
    order = sorted(list)
    return list.get(order[1])
