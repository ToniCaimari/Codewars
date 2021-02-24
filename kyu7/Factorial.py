def factorial(n):
    if n < 0:
        raise ValueError
    if n > 12:
        raise ValueError
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result
