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
    teszt(sajat_osszeg([1, 2, 3, 4]) == 10)
    teszt(sajat_osszeg([1.25, 2.5, 1.75]) == 5.5)
    teszt(sajat_osszeg([1, -2, 3]) == 2)
    teszt(sajat_osszeg([ ]) == 0)
    teszt(sajat_osszeg(range(11)) == 55) # A 11 nem eleme a listának.

    
def sajat_osszeg(xs):
    """[Az xs lista elemeinek összegzése és az eredmény visszaadása]

    Args:
        xs ([type]): [description]
    """
    futo_osszeg = 0
    for x in xs:
        futo_osszeg = futo_osszeg + x
    return futo_osszeg

tesztkeszlet()