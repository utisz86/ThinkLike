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
    teszt(rek_max([2, 9, [1, 13], 8, 6]) == 13)
    teszt(rek_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
    teszt(rek_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
    teszt(rek_max(["jancsi", ["sanyi", "bence"]]) == "sanyi")


def rek_szum(beagyazott_lista):
    ossz = 0
    for elem in beagyazott_lista:
        if type(elem) == type([]):
            ossz += rek_szum(elem)
        else:
            ossz += elem
    return ossz


def rek_max(nxs):
    """[Keresd meg a maximumot rekurzív módon egy beágyazott listában. El˝ofeltétel: A listák vagy részlisták nem üresek.]

    Args:
        nxs ([type]): [description]
    """
    legnagyobb = None
    elso_alk = True
    for e in nxs:
        if type(e) == type([]):
            ert = rek_max(e)
        else:
            ert = e

        if elso_alk or ert > legnagyobb:
            legnagyobb = ert
            elso_alk = False

    return legnagyobb

def rekurzio_melysege(szam):
    print("{0}, ".format(szam), end="")
    rekurzio_melysege(szam + 1)



tesztkeszlet()