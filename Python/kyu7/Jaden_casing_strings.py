def to_jaden_case(string):
    jaden_string = string.title()
    alert = 0
    response = ''
    for i in jaden_string:
        if alert == 0:
            if i != "'":
                response += i
            else:
                response += i
                alert += 1
        else:
            alert -= 1
            response += i.lower()

    return response
