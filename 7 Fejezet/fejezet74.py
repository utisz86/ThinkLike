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
    teszt(nulla_es_ot_szamjegy_szam(1055030250) == 7)
    teszt(szamjegy_szam(0) == 1)

def szamjegy_szam(n):
    szamlalo = 0
    while n != 0:
        szamlalo += 1
        n = n //10
    return szamlalo

print(szamjegy_szam(710))

def nulla_es_ot_szamjegy_szam(n):
    szamlalo = 0
    while n > 0:
        szamjegy = n % 10
        if szamjegy == 0 or szamjegy == 5:
            szamlalo += 1
        n = n // 10
    return szamlalo

tesztkeszlet()