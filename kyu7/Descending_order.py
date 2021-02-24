def descending_order(num):
    list = []
    S_num = str(num)
    for i in S_num:
        list.append(i)
    S = sorted(list)
    J = ''.join(S)
    X = J[::-1]
    result = int(X)
    return result
