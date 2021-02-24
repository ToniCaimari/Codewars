def xo(s):
    g_list = s.lower()
    list_x = []
    list_o = []
    for i in g_list:
        if i == 'x':
            list_x.append(i)
        if i == 'o':
            list_o.append(i)
    if len(list_x) == len(list_o):
        return True
    else:
        return False
