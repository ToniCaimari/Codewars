def diamond(n):
    if n % 2 == 0:
        return None
    if n < 0:
        return None
    x = []
    space = ' '
    while n >= 1:
        if len(x) != 0:
            x.append(space+('*'*n)+'\n')
            n -= 2
            space += ' '
        else:
            x.append(('*'*n)+'\n')
            n -= 2
    inverted_x = x[::-1]
    inverted_x.pop()
    macro = inverted_x+x
    response = ''
    for i in macro:
        response += i
    return response
