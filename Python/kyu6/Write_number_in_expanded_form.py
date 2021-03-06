def expanded_form(num):
    n = 1
    reverse = str(num)[::-1]
    list = []
    response = ''
    for i in reverse:
        if int(i) != 0:
            list.append(int(i)*n)
            n *= 10
        else:
            n *= 10
            continue
    if len(list) > 1:
        for i in list[::-1]:
            response += str(i)+' + '
        return response[:len(response)-3]
    else:
        return str(list.pop())
