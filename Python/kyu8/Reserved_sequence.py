def reverse_seq(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    return sorted(list, reverse=True)
