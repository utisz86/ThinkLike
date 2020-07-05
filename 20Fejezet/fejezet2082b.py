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
    # Futasd ezeket a teszteket...
    uj_keszlet = {}
    plusz_gyumolcs(uj_keszlet, "eper", 10)
    teszt("eper" in uj_keszlet)
    teszt(uj_keszlet["eper"] == 10)
    plusz_gyumolcs(uj_keszlet, "eper", 25)
    teszt(uj_keszlet["eper"] == 35)



def plusz_gyumolcs(keszlet, gyumolcs, mennyiseg=0):
    if gyumolcs not in keszlet:
        keszlet[gyumolcs] = mennyiseg
    else:
        keszlet[gyumolcs] += mennyiseg

tesztkeszlet()
