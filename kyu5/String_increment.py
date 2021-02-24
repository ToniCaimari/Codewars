def increment_string(strng):
    rev_strng = strng[::-1]
    digit_l = []
    str_l = ""
    alert = False
    for i in rev_strng:
        if i.isdigit() == True:
            if alert == False:
                digit_l.append(i)
            else:
                str_l += i
        else:
            str_l += i
            alert = True
    real_digit_l = digit_l[::-1]
    real_str_l = str_l[::-1]
    if len(digit_l) != 0:
        n = int(''.join(real_digit_l))+1
        num_digit = str(n).zfill(len(digit_l))
        return real_str_l+str(num_digit)
    else:
        return real_str_l+'1'
