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
    teszt(ugyanazon_az_atlon(5,2,2,0) == False)
    teszt(ugyanazon_az_atlon(5,2,3,0) == True)
    teszt(ugyanazon_az_atlon(5,2,4,3) == True)
    teszt(ugyanazon_az_atlon(5,2,4,1) == True)
    # Olyan megoldási esetek, amikor nincsenek ütközések
    teszt(oszlop_utkozes([6,4,2,0,5], 4) == False)
    teszt(oszlop_utkozes([6,4,2,0,5,7,1,3], 7) == False)
    # További tesztesetek, amikor többnyire ütközések vannak
    teszt(oszlop_utkozes([0,1], 1) == True)
    teszt(oszlop_utkozes([5,6], 1) == True)
    teszt(oszlop_utkozes([6,5], 1) == True)
    teszt(oszlop_utkozes([0,6,4,3], 3) == True)
    teszt(oszlop_utkozes([5,0,7], 2) == True)
    teszt(oszlop_utkozes([2,0,1,3], 1) == False)
    teszt(oszlop_utkozes([2,0,1,3], 2) == True)
    #
    teszt(van_utkozes([6,4,2,0,5,7,1,3]) == False) # A fenti megoldás
    teszt(van_utkozes([4,6,2,0,5,7,1,3]) == True) # Felcseréljük az els˝o két sort
    teszt(van_utkozes([0,1,2,3]) == True) # Kipróbáljuk egy 4x4 sakktáblán
    teszt(van_utkozes([2,0,3,1]) == False) # Megoldás 4x4-es esetben



def ugyanazon_az_atlon(x0, y0, x1, y1):
    """[Az (x0, y0) királyn˝o ugyanazon az átlón van-e (x1, y1) királyn˝ovel?]

    Args:
        x0 ([type]): [description]
        y0 ([type]): [description]
        x1 ([type]): [description]
        y1 ([type]): [description]
    """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dx == dy     # Ütköznek, ha dx == dy


def oszlop_utkozes(bs, c):
    """[True-val tér vissza, hogyha a c oszlopban lév˝o királyn˝o ütközik a t˝ole balra lev˝okkel.]

    Args:
        bs ([type]): [description]
        c ([type]): [description]
    """
    for i in range(c):  # Nézd meg az összes oszlopot a c-t˝ol balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True
    return False        # Nincs ütközés, a c oszlopban biztonságos helyen van


def van_utkozes(sakktabla):
    """[Meghatározzuk, hogy van-e rivális az átlóban. Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak, ezért nem kifejezetten ellen˝orizzük a sor vagy oszlop ütközéseket.]

    Args:
        sakktabla ([type]): [description]
    """
    for col in range(1, len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False

tesztkeszlet()
