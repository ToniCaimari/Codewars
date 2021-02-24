def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    list = []

    response = []
    for i in range(a, b+1):
        if i >= 10:
            list.append(str(i))
            continue
        if i > 0:
            response.append(i)
            continue
    for i in list:
        end = 0
        power = 1
        for c in i:
            end += int(c)**power
            power += 1
        if int(i) == end:
            response.append(int(i))
            end -= end
            power = 1
        if int(i) != end:
            end -= end
            power = 1

    return response
