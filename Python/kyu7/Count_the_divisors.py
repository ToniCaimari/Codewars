def divisors(n):
    contador = 0
    for d in range(1, n+1):
        if d <= n:
            if n % d == 0:
                contador += 1
    return contador
