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
    teszt(linearis_kereses(baratok, "Zoltán") == 1)
    teszt(linearis_kereses(baratok, "Péter") == 0)
    teszt(linearis_kereses(baratok, "Panni") == 6)
    teszt(linearis_kereses(baratok, "Béla") == -1)
    #
    szokincs = ["alma", "esett", "f˝ure", "fáról", "alá", "a", "fel"]
    konyv_szavai = "az alma a fáról le esett a f˝ure".split()
    teszt(ismeretlen_szavak_keresese(szokincs, konyv_szavai) == ["az", "le"])
    teszt(ismeretlen_szavak_keresese([], konyv_szavai) == konyv_szavai)
    teszt(ismeretlen_szavak_keresese(szokincs, ["alma", "alá", "esett"]) == [])
    #
    teszt(szovegbol_szavak("Az én nevem Alice!") == ["az", "én", "nevem", "alice"])
    teszt(szovegbol_szavak('"Nem, Én soha!", mondta Alice.') == ["nem", "én", "soha", "mondta", "alice"])


def linearis_kereses(xs, ertek):
    """[Keresse meg és térjen vissza az érték indexével az xs sorozatban]

    Args:
        xs ([type]): [description]
        ertek ([type]): [description]
    """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1

def ismeretlen_szavak_keresese(szokincs, szavak):
    """[Visszatérünk a könyv azon szavainak listájával, amelyek nincsenek benne a szókincsben.]

    Args:
        szokincs ([type]): [description]
        szavak ([type]): [description]
    """
    eredmeny = []
    for w in szavak:
        if (linearis_kereses(szokincs, w) < 0):
            eredmeny.append(w)
    return eredmeny
    

def szavak_betoltese_fajlbol(fajlnev):
    """[Szavak olvasása a megadott fájlból, visszatér a szavak listájával]

    Args:
        fajlnev ([type]): [description]
    """
    f = open(fajlnev, "r")
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak
    
nagyobb_szokincs = szavak_betoltese_fajlbol("vocab.txt")
print("A szókincsben {0} szó található, kezdve: \n {1} ".format(len(nagyobb_szokincs), nagyobb_szokincs[:6]))

def szovegbol_szavak(szoveg):
    """[Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden szót kisbet˝ussé alakít.]

    Args:
        szoveg ([type]): [description]
    """
    # Ha bármelyikükkel találkozol
    # Cseréld ˝oket ezekre
    helyettesites = szoveg.maketrans( "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\", "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"+42*" ")
    # Most alakítsd át a szöveget
    tisztitott_szoveg = szoveg.translate(helyettesites)
    szavak = tisztitott_szoveg.split()
    return szavak

def szavak_a_konyvbol(fajlnev):
    """[Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját]

    Args:
        fajlnev ([type]): [description]
    """
    f = open(fajlnev, "r")
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak

konyv_szavai = szavak_a_konyvbol("alice_in_wonderland.txt")
print("A könyvben {0} szó található, az els˝o 100 a következ˝o:\n{1}".format(len(konyv_szavai), konyv_szavai[:100]))

tesztkeszlet()

import time
t0 = time.process_time()
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
t1 = time.process_time()
print(hianyzo_szavak)
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))




