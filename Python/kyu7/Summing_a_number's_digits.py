def sum_digits(number):
    n = [int(i) for i in str(abs(number))]
    return sum(n)
