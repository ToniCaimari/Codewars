def series_sum(n):
    sum = 0
    acum = 1
    while n > 0:
        sum += 1/acum
        acum += 3
        n -= 1
    return str(format(sum, '.2f'))
