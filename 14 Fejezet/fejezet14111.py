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
    # A
    teszt(osszefesul_mindketto(xs, []) == [])
    teszt(osszefesul_mindketto([], ys) == [])
    teszt(osszefesul_mindketto([], []) == [])
    teszt(osszefesul_mindketto(xs, ys) == [])
    teszt(osszefesul_mindketto([1,2,3], [3,4,5]) == [3])
    teszt(osszefesul_mindketto(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) == ["cica"])
    # B
    teszt(osszefesul_elso(xs, []) == xs)
    teszt(osszefesul_elso([], ys) == [])
    teszt(osszefesul_elso([], []) == [])
    teszt(osszefesul_elso(xs, ys) == xs)
    teszt(osszefesul_elso([1,2,3], [3,4,5]) == [1,2])
    teszt(osszefesul_elso(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) == ["egér", "kutya"])
    # C
    teszt(osszefesul_masodik(xs, []) == [])
    teszt(osszefesul_masodik([], ys) == ys)
    teszt(osszefesul_masodik([], []) == [])
    teszt(osszefesul_masodik(xs, ys) == ys)
    teszt(osszefesul_masodik([1,2,3], [3,4,5]) == [4,5])
    teszt(osszefesul_masodik(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) == ["kakas", "medve"])
    # D
    teszt(osszefesul_elsovmasodik(xs, []) == xs)
    teszt(osszefesul_elsovmasodik([], ys) == ys)
    teszt(osszefesul_elsovmasodik([], []) == [])
    teszt(osszefesul_elsovmasodik(xs, ys) == zs)
    teszt(osszefesul_elsovmasodik([1,2,3], [3,4,5]) == [1,2,4,5])
    teszt(osszefesul_elsovmasodik(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) == ["egér", "kakas", "kutya", "medve"])
    # E
    teszt(osszefesul_elsominusmasodik(xs, []) == xs)
    teszt(osszefesul_elsominusmasodik([], ys) == [])
    teszt(osszefesul_elsominusmasodik([], []) == [])
    teszt(osszefesul_elsominusmasodik(xs, ys) == xs)
    teszt(osszefesul_elsominusmasodik([1,2,3], [3,4,5]) == [1,2])
    teszt(osszefesul_elsominusmasodik([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])
    teszt(osszefesul_elsominusmasodik(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) == ["cica", "egér", "kakas", "kutya", "medve"])

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

# A
def osszefesul_mindketto(xs, ys):
    """[Csak azokat az elemeket adja vissza, melyek mindkét listába benne vannak.]

    Args:
        xs ([type]): [description]
        ys ([type]): [description]
    """
    eredmeny = []
    xi = 0

    while True:
        if xi >= len(xs):               # Ha az xs lista végére értünk
            return eredmeny             # Készen vagyunk
        
        if xi >= len(ys):               # Ugyanaz, csak fordítva
            return eredmeny

        # Ha mindkét listában vannak még elemek, akkor a kisebbik elemet másoljuk az eredmény listába, ha meg egyezik
        if len(xs) <= len(ys):
            if xs[xi] in ys:
                eredmeny.append(xs[xi])
        else:
            if ys[xi] in xs:
                eredmeny.append(ys[xi])
        
        xi += 1


# B
def osszefesul_elso(xs, ys):
    """[Csak azokat az elemeket adja vissza, melyek benne vannak az els˝o listában, de nincsenek benne a másodikban.]

    Args:
        xs ([type]): [description]
        ys ([type]): [description]
    """
    eredmeny = []

    for element in xs:
        if element not in ys:
            eredmeny.append(element)
    return eredmeny 


# C
def osszefesul_masodik(xs, ys):
    """[Csak azokat az elemeket adja vissza, melyek benne vannak a második listában, de nincsenek az els˝oben.]

    Args:
        parameter_list ([type]): [description]
    """
    eredmeny = []

    for element in ys:
        if element not in xs:
            eredmeny.append(element)
    return eredmeny 

# D
def osszefesul_elsovmasodik(xs, ys):
    """[Csak azokat az elemeket adja vissza, melyek vagy az els˝oben vagy a másodikban vannak benne.]

    Args:
        xs ([type]): [description]
        ys ([type]): [description]
    """
    eredmeny = []
    for elem in xs:
        if elem not in ys:
            eredmeny.append(elem)

    for elem in ys:
        if elem not in xs:
            eredmeny.append(elem)

    eredmeny.sort()
    return eredmeny


# E
def osszefesul_elsominusmasodik(xs, ys):
    """[Azokat az elemeket adja vissza az els˝o listából, amelyeket a második lista egy megegyez˝o eleme nem
távolít el. Ebben az esetben a második lista egyik eleme „kiüti” az els˝o listában szerepl˝o elemet. Például
kivonas([5,7,11,11,11,12,13], [7,8,11]) visszaadja következ˝o listát: [5,11,11,12,
13].]

    Args:
        xs ([type]): [description]
        ys ([type]): [description]
    """
    return  [x for x in xs if x not in ys]

tesztkeszlet()

