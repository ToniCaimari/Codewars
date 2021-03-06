def delete_nth(order, max_e):
    list = []
    for i in order:
        if list.count(i) == 0:
            list.append(i)
            continue
        if list.count(i) < max_e:
            list.append(i)
            continue

    return list
