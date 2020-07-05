import sys

def teszt(sikeres_teszt):
    """ Egy test eredmenyenek megjelenitese.    """
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z) {0}. sorban allo teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban allo teszt SIKERTELEN".format(sorszam))

    print(msg)

def tesztkeszlet():
    """ Az ehhez a modulhoz (fajlhoz) tartozo tesztkeszlet futtatasa. """
    teszt(abs(-5) == 5)
    # 0, 1, 1, 2, 3, 5, 8, 13
    teszt(fib(0) == 0)
    teszt(fib(1) == 1)
    teszt(fib(2) == 1)
    teszt(fib(3) == 2)
    teszt(fib(7) == 13)
    # fib2
    teszt(fib2(0) == 0)
    teszt(fib2(1) == 1)
    teszt(fib2(2) == 1)
    teszt(fib2(3) == 2)
    teszt(fib2(7) == 13)


def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    n0 = 1
    n1 = 1
    eredmeny = 0
    for i in range(2, n):
        eredmeny = n0 + n1
        n0 = n1
        n1 = eredmeny

    return eredmeny



tesztkeszlet()
