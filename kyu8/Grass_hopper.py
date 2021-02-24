def summation(num):
    list = []
    for i in range(1, num+1):
        if i <= num:  # numero original
            list.append(i)
    return sum(list)
