def capitalize(s):
    frase1 = ""
    frase2 = ""
    list = []
    upp_low = False
    for i in s:
        if upp_low == False:
            frase1 += i.upper()
            frase2 += i
            upp_low = True
            continue
        if upp_low == True:
            frase1 += i
            frase2 += i.upper()
            upp_low = False
            continue
    list.append(frase1)
    list.append(frase2)
    return list
