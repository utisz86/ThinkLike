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
    # haromszog
    teszt(haromszog(-5) == None)
    teszt(haromszog(1) == 1)
    teszt(haromszog(5) == 15)
    teszt(haromszog(10) == 55)
    teszt(haromszog(11) == 66)

# 7.9.26.9
# A
def haromszogszamok(n):
    """[Írj egy haromszogszamok nev˝u függvényt, amely kiírja az els˝o n darab háromszögszámot! A
haromszogszamok(5) hívás ezt a kimenetet eredményezi:]

    Args:
        n ([type]): [description]
    """
    for i in range(1,n+1):
        print(i,"\t",haromszog(i))
    

# B
# N-edik haromszogszam
def haromszog(n):
    """[N-edik haromszogszam]

    Args:
        n ([type]): [description]
    """
    if not(isinstance(n, int)):
        return None
    elif n >= 1:
        return int((n *(n + 1))/2)
    else:
        return None


tesztkeszlet()

haromszogszamok(5)