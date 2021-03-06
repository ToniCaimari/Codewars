def duplicate_encode(input):
    respuesta = ""
    input_l = input.lower()
    for i in input_l:
        if input_l.count(i) == 1:
            respuesta += '('
        else:
            respuesta += ')'
    return respuesta
