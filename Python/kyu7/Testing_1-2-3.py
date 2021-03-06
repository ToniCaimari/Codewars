def number(lines):
    response = []
    pos = 1
    for i in lines:
        response.append(str(pos)+': '+i)
        pos += 1
    return response
