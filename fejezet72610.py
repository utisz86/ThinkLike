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
    #
    teszt(prim_e(2))
    teszt(prim_e(3))
    teszt(prim_e(5))
    teszt(not(prim_e(6)))
    teszt(prim_e(11))
    teszt(not prim_e(35))
    teszt(not(prim_e(19860922)))

def prim_e(n):
    """[Írj egy prim_e függvényt, amely kap egy egészet paraméterként és True értéket ad vissza, ha a paramétere
egy prímszám és False értéket különben! Adj hozzá ilyen teszteket:]

    Args:
        n ([type]): [description]
    """
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    t = 3
    while True:
        if t == n:
            return True

        if n % t == 0:
            return False

        t += 2
        


tesztkeszlet()

prim_e(19981121)