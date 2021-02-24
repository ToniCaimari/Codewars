def longest(s1, s2):
    result = ""
    list = []
    for i in s1:
        if i not in list:
            list.append(i)
    for i in s2:
        if i not in list:
            list.append(i)
    s_list = sorted(list)
    for i in s_list:
        result += i

    return result
