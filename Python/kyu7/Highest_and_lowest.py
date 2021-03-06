def high_and_low(numbers):
    print(numbers)
    list = []
    r = ""
    n = numbers.split()
    for i in n:
        list.append(int(i))
    s_list = sorted(list)
    a = str(s_list.pop())
    if len(s_list) == 0:
        return a+" "+a
    b = str(s_list[0])
    r = a+" "+b
    return r
