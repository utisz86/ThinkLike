mar_ismert = {0: 0, 1: 1}

def fib(n):
    if n not in mar_ismert:
        uj_ertek = fib(n-1) + fib(n-2)
        mar_ismert[n] = uj_ertek
    return mar_ismert[n]

print(fib(100))    