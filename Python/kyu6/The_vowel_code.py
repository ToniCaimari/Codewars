vowel = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}


def encode(st):
    cod_st = ''
    for i in st:
        if i in vowel:
            for key, value in vowel.items():
                if i == key:
                    cod_st += str(value)
                    continue
        else:
            cod_st += i
            continue
    return cod_st


def decode(st):
    cod_st = ''
    for i in st:
        if i.isdigit() == True:
            for key, value in vowel.items():
                if int(i) == value:
                    cod_st += key
                    continue

        else:
            cod_st += i
            continue
    return cod_st
