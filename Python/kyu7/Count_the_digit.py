def nb_dig(n, d):
    list = ''
    for i in range(0, n+1):
        list += str(i*i)
    return list.count(str(d))
