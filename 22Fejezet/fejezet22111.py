from ido_class import Ido 

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
    # kozte_van_e(i1, i2, i3)
    teszt(kozte_van_e(Ido(9,1,1), Ido(9,1,2), Ido(9,1,3)))
    teszt( not kozte_van_e(Ido(9,1,1), Ido(10,1,2), Ido(9,1,3)))


def kozte_van_e(i1, i2, i3):
    """[summÍrj egy kozte_van_e logikai függvényt, amely három Ido objektumot vár paraméterként (obj, i1, i2), és True értéket ad vissza, ha az els˝o paraméterben kapott id˝opont a másik kett˝o közé esik. Feltételezhet˝o, hogy az i1 <= i2. Az id˝opontok által meghatározott tartományt aluról zártnak, felülr˝ol nyitottnak tekintjük, tehát akkor térjen vissza igazzal a függvény, ha az alábbi kifejezés teljesül: i1 <= obj < i2.ary]

    Args:
        i1 ([type]): [description]
        i2 ([type]): [description]
        i3 ([type]): [description]
    """
    if i1.masodpercre_valtas() < i2.masodpercre_valtas():
        if i2.masodpercre_valtas() < i3.masodpercre_valtas():
            return True
    else:
        return False

    


tesztkeszlet()

if Ido(10,1,1) > Ido(9,1,2):
    print("Ok")

if Ido(9,1,1) == Ido(9,1,1):
    print("Ok")