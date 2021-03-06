def print_nums(*n):
    response = ''
    list = []
    l_n = sorted(n)
    for i in n:
        list.append(str(i).zfill(len(str(l_n[-1]))))
    for i in list:
        if len(response) == 0:
            response += i
        else:
            response += '\n'+i
    return response
