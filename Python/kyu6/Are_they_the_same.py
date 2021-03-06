def comp(array1, array2):
    if not array1:
        if not array2:
            if array1 is None:
                return False
            if array2 is None:
                return False
    for i in array1:
        if i*i in array2:
            array2.remove(i*i)
            continue
        else:
            return False
    for i in array2:
        return False
    return True
