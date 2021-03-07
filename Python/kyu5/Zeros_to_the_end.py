def move_zeros(array):
    list_A = []
    list_B = []
    for i in array:
        if i != 0:
            list_A.append(i)
        else:
            list_B.append(i)
    return list_A+list_B
