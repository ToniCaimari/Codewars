def accum(s):
    alert = True
    turn = 1
    pre_response = ''
    response = ''
    for i in s:
        pre_response += i*turn+'-'
        turn += 1
    for i in pre_response:
        if alert == False:
            if i != '-':
                response += i.lower()
            else:
                alert = True
                response += i
        else:
            response += i.upper()
            alert = False
    return response[:-1]
