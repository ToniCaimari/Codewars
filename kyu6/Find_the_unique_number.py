def find_uniq(arr):
    li = sorted(arr)
    for n in li:
        if li[0] == li[1]:
            return li.pop()
        else:
            return li[0]
