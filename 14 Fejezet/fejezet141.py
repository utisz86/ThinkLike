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
    baratok = ["Péter", "Zoltán", "János", "Kata", "Zita", "Sándor", "Panni"]
    teszt(teljes_kereses(baratok, "Zoltán") == 1)
    teszt(teljes_kereses(baratok, "Péter") == 0)
    teszt(teljes_kereses(baratok, "Panni") == 6)
    teszt(teljes_kereses(baratok, "Béla") == -1)


def teljes_kereses(xs, ertek):
    """[Keresse meg és térjen vissza az érték indexével az xs sorozatban]

    Args:
        xs ([type]): [description]
        ertek ([type]): [description]
    """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1
    

tesztkeszlet()
