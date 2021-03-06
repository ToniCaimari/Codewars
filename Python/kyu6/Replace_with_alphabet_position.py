import string


def alphabet_position(text):
    albz = string.ascii_lowercase
    list = ''
    resp_l = []
    resp = ''
    for i in text.lower():
        if i.isalpha() == True:
            list += i
        else:
            continue
    for i in list:
        resp_l.append(str(albz.index(i)+1))
    for i in resp_l:
        resp += i+' '
    return resp[: -1]
