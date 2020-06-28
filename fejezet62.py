""" 
Hogyan gondolkozz úgy, mint egy
informatikus:
Tanulás Python 3 segítségével
6.9. Feladatok
"""

# Import moduls
import sys

# Teszt fugyveny
def teszt(sikeres_teszt):
    """Egy teszt eredmenyenek megjelenitese

    Args:
        sikeres_teszt (Boolean): a teszt eredmenye True/False
    """
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z) {0}. sorban allo teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban allo teszt SIKERTELEN".format(sorszam))

    print(msg)

# Teszt keszlet
def tesztkeszlet():
    """A teszteles soran vegrehajtott tesztek
    """
    # Alap teszt
    teszt(abs(17) == 17)
    # Tovabbi tesztek
    # 6.9.1
    teszt(fordulj_orajarasi_iranyba("É") == "K")
    teszt(fordulj_orajarasi_iranyba("Ny") == "É")
    teszt(fordulj_orajarasi_iranyba(42) == None)
    teszt(fordulj_orajarasi_iranyba("ostobaság") == None)
    # 6.9.2
    teszt(nap_nev(3) == "csütörtök")
    teszt(nap_nev(6) == "vasárnap")
    teszt(nap_nev(42) == None)
    teszt(nap_nev("3") == None)

# 6.9.1 feladat
def fordulj_orajarasi_iranyba(tajegyseg):
    """A négy tájegységet rövidítse: „K” , „Ny” , „É”, „D”. Írj egy fordulj_orajarasi_iranyba függvényt,
amely egy tájegységet leíró karakter rövidítését várja, és visszaadja az órajárási irányban nézve szomszédos
égtáj rövidítését. Itt van néhány tesztest, melyre m˝uködnie kell a függvényednek:

    Args:
        tajegyseg (string): [description]

    Returns:
        string: „K” , „Ny” , „É”, „D”.
    """
    if tajegyseg == "K":
        return "D"
    elif tajegyseg == "Ny":
        return "É"
    elif tajegyseg == "É":
        return "K"
    elif tajegyseg == "D":
        return "Ny"
    else:
        return None


# 6.9.2 feladat nap_nev fuggveny
def nap_nev(nap_szam):
    napok = ["hétfő", "Kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
    if type(nap_szam) != int:
        return None
    elif nap_szam >= 0 and nap_szam <= 6:
        return napok[nap_szam]
    else:
        return None


# Tesztvegrehajtasa
tesztkeszlet()