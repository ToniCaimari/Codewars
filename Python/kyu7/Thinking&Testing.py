def testit(a, b):
    print(a, b)
    r = []
    z = []
    for i in a:
        if i not in r:
            r.append(i)
    for i in b:
        if i not in z:
            z.append(i)
    r.extend(z)  # extend???
    return sorted(r)
