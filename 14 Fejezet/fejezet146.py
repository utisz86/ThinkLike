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
    xs = [1,3,5,7,9,11,13,15,17,19]
    ys = [4,8,12,16,20,24]
    zs = xs+ys
    zs.sort()
    teszt(osszefesul(xs, []) == xs)
    teszt(osszefesul([], ys) == ys)
    teszt(osszefesul([], []) == [])
    teszt(osszefesul(xs, ys) == zs)
    teszt(osszefesul([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
    teszt(osszefesul(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) == ["cica", "cica", "egér", "kakas", "kutya", "medve"])

def osszefesul(xs, ys):
    """[Összefésüli a rendezett xs és ys listákat. Visszatér a rendezett eredménnyel]

    Args:
        xs ([type]): [description]
        ys ([type]): [description]
    """
    eredmeny = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):               # Ha az xs lista végére értünk
            eredmeny.extend(ys[yi:])    # Még vannak elemek az ys listában
            return eredmeny             # Készen vagyunk
        
        if yi >= len(ys):               # Ugyanaz, csak fordítva
            eredmeny.extend(xs[xi:])
            return eredmeny

        # Ha mindkét listában vannak még elemek, akkor a kisebbik elemet másoljuk az eredmény listába
        if xs[xi] <= ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
        else:
            eredmeny.append(ys[yi])
            yi += 1

def ismeretlen_szavak_osszefesulessel(szokincs, szavak):
    """[Mind a szókincs és könyv szavai rendezettek kell, legyenek. Visszatérünk egy új szólistával, mely szavak benne vannak a könyvben, de nincsenek a szókincsben.]

    Args:
        szokincs ([type]): [description]
        szavak ([type]): [description]
    """
    eredmeny = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(szokincs):
            eredmeny.extend(szavak[yi:])

        if yi >= len(szavak):
            return eredmeny

        if szokincs[xi] == szavak[yi]: # A szó benne van a szókincsben
            yi += 1

        elif szokincs[xi] < szavak[yi]: # Haladjon tovább
            xi += 1
        
        else:                           # Találtunk olyan szót, mely nincs a szókincsben
            eredmeny.append(szavak[yi])
            yi += 1
            

tesztkeszlet()

from fejezet145 import szomszedos_dupl_eltovolit as szomszedos_dupl_eltovolit
from fejezet145 import osszes_szo as osszes_szo
from fejezet145 import nagyobb_szokincs as nagyobb_szokincs
from fejezet145 import konyv_szavai as konyv_szavai


import time

osszes_szo = osszes_szo
t0 = time.process_time()
osszes_szo.sort()
konyv_szavai = szomszedos_dupl_eltovolit(osszes_szo)
hianyzo_szavak = ismeretlen_szavak_osszefesulessel(nagyobb_szokincs, konyv_szavai)
t1 = time.process_time()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))
