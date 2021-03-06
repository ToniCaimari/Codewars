def iq_test(numbers):
    splt = numbers.split()
    list = [int(i) for i in splt]
    par = []
    impar = []
    for i in list:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)

    if len(par) == 1:
        return splt.index(str(par.pop()))+1
    if len(impar) == 1:
        return splt.index(str(impar.pop()))+1
