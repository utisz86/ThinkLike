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
    xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
    teszt(binaris_kereses(xs, 20) == -1)
    teszt(binaris_kereses(xs, 99) == -1)
    teszt(binaris_kereses(xs, 1) == -1)
    for (i, v) in enumerate(xs):
        teszt(binaris_kereses(xs, v) == i)
    #
    teszt(szomszedos_dupl_eltovolit([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
    teszt(szomszedos_dupl_eltovolit([]) == [])
    teszt(szomszedos_dupl_eltovolit(["egy", "kis", "kis", "kölyök", "kutya"]) == ["egy", "kis", "kölyök", "kutya"])




def binaris_kereses(xs, ertek):
    """[Keressük meg és térjünk vissza az érték indexével az xs sorozatban]

    Args:
        xs ([type]): [description]
        ertek ([type]): [description]
    """
    ah = 0
    fh = len(xs)
    while True:
        if ah == fh:    # Ha a vizsgált terület üres
            return -1

        # A következ˝o összehasonlítás a ROI közepén kell legyen
        kozep_index = (ah + fh) // 2

        # Fogjuk középs˝o indexen lév˝o elemet
        kozep_elem = xs[kozep_index]

        #print("ROI[{0}:{1}](méret={2}), próba='{3}', érték='{4}'"
        # .format(ah, fh, fh-ah, kozep_elem, ertek))

        # Hasonlítsuk össze az elemet az adott pozícióban lév˝ovel

        if kozep_elem == ertek:
            return kozep_index      # Megtaláltuk!
        if kozep_elem < ertek:
            ah = kozep_index + 1    # Használjuk a fels˝o ROI-t
        else:
            fh = kozep_index        # Használjuk az alsó ROI-t

def ismeretlen_szavak_keresese(szokincs, szavak):
    """[Visszatérünk a könyv azon szavainak listájával, amelyek nincsenek benne a szókincsben.]

    Args:
        szokincs ([type]): [description]
        szavak ([type]): [description]
    """
    eredmeny = []
    for w in szavak:
        if (binaris_kereses(szokincs, w) < 0):
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

def szomszedos_dupl_eltovolit(xs):
    """[Visszatér egy új listával, amelyben a szomszédos
3 duplikátumok el vannak távolítva az xs listából.]

    Args:
        xs ([type]): [description]
    """
    eredmeny = []
    aktualis_elem = None
    for e in xs:
        if e != aktualis_elem:
            eredmeny.append(e)
            aktualis_elem = e
    return eredmeny
            

konyv_szavai = szavak_a_konyvbol("alice_in_wonderland.txt")
print("A könyvben {0} szó található, az els˝o 100 a következ˝o:\n{1}".format(len(konyv_szavai), konyv_szavai[:100]))

tesztkeszlet()

import time

t0 = time.process_time()
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
t1 = time.process_time()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))

osszes_szo = szavak_a_konyvbol("alice_in_wonderland.txt")
osszes_szo.sort()
konyv_szavai = szomszedos_dupl_eltovolit(osszes_szo)
print("A könyvben {0} szó van. Csak {1} egyedi.".format(len(osszes_szo), len(konyv_szavai)))

print("Az els˝o 100 szó\n{0}".format(konyv_szavai[:100]))

t0 = time.process_time()
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
t1 = time.process_time()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))