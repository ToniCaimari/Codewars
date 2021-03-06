def century(year):
    if year % 100 == 0:
        cent = year//100
        return cent
    else:
        cent = year//100+1
        return cent
