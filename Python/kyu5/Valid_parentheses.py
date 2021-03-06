def valid_parentheses(string):
    if not string:
        return True
    alert = 0
    start = True
    st = ''
    for i in string:
        if i == '(':
            st += i
        if i == ')':
            st += i

    if st.count('(') == st.count(')'):
        for i in st:
            if start == True:
                if i == '(':
                    alert += 1
                    start = False
                else:
                    return False
            else:
                if i == '(':
                    alert += 1
                else:
                    if alert > 0:
                        alert -= 1
        if alert == 0:
            return True
        else:
            return False
    else:
        return False
