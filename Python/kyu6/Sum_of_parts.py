def parts_sums(ls):
    list = [sum(ls)]
    n = 0
    position = 0
    for i in ls:
        list.append(list[position]-i)
        n += i
        position += 1
    return list
