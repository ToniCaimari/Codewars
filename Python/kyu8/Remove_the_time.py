def shorten_to_date(long_date):
    result = ''
    for i in long_date:
        if i != ',':
            result += i
        else:
            break
    return result
