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
    # 11.22.10
    teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")
    s = "Kerek a gömb, gömbszerű!"
    teszt(cserel(s, "öm", "om") == "Kerek a gomb, gombszerű!")
    teszt(cserel(s, "o", "ö") == "Kerek a gömb, gömbszerű!")


# 11.22.10
def cserel(s, regi, uj):
    """[Írj egy cserel(s, regi, uj) függvényt, amely kicseréli a regi összes el˝ofordulását a uj-ra az s szrtingben.]

    Args:
        s ([type]): [description]
        regi ([type]): [description]
        uj ([type]): [description]
    """
    uj_s = s.replace(regi, uj)

    return uj_s

tesztkeszlet()
