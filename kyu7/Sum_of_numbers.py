def get_sum(a, b):
    list = []
    suma = 0
    list.append(a)
    list.append(b)
    list_ord = sorted(list)
    n = list_ord[0]
    m = list_ord[1]
    for i in range(n, m+1):
        suma += i
    return suma
