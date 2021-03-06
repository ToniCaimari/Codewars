def printer_error(s):
    count = 0
    a_m = 'abcdefghijklm'
    for i in s:
        if i in a_m:
            continue
        else:
            count += 1
    return str(count)+'/'+str(len(s))
