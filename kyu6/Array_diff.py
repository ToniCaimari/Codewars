def array_diff(a, b):
    rest = []
    for i in a:
        rest.append(i)
    for i in a:
        if i == i in b:
            rest.remove(i)
    return rest
