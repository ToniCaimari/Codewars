def up_array(arr):
    if len(arr) == 0:
        return None
    for i in arr:
        if i < 0:
            return None
        if i > 9:
            return None
    str_l = ""
    resp = []
    for i in arr:
        str_l += str(i)
    num = str(int(str_l)+1)
    for i in num:
        resp.append(int(i))
    return resp
