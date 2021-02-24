def to_camel_case(text):
    list = ''
    response = ''
    for i in text:
        if i.isalpha() == True:
            list += i
        else:
            if i == '-' or '_':
                list += '.'
    list = list.split('.')
    for i in list:
        if i != list[0]:
            response += i.title()
        else:
            response += i
    return response
