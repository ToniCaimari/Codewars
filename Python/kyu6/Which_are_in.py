def in_array(a1, a2):
    r = []
    for i in a1:
        if any(i in s for s in a2):
            if i not in r:
                r.append(i)
    return sorted(r)
