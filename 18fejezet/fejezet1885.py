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
    # rekurziv_min
    teszt(rekurziv_min([2, 9, [1, 13], 8, 6]) == 1)
    teszt(rekurziv_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    teszt(rekurziv_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    teszt(rekurziv_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

    # szamol
    teszt(szamol(2, []) == 0)
    teszt(szamol(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    teszt(szamol(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    teszt(szamol(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    teszt(szamol(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    teszt(szamol("a", [["ez",["a",["keres","a"],"a"],"nagyon"], ["a","konnyu"]]) == 4)

    # kisimit
    teszt(kisimit([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    teszt(kisimit([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    teszt(kisimit([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
    teszt(kisimit([["ez",["a",["keres"],"a"],"nagyon"],["a","konnyu"]]) ==
    ["ez","a","keres","a","nagyon","a","konnyu"])
    teszt(kisimit([]) == [])

def rekurziv_min(nxs):
    """[Írj egy rekurziv_min függvényt, amely a visszaadja a beágyazott lista legkisebb elemét. Feltételezzük, hogy a lista vagy a részlista nem üres:]

    Args:
        lista ([type]): [description]
    """
    legkisebb = None
    elso_alk = True
    for e in nxs:
        if type(e) == type([]):
            ert = rekurziv_min(e)
        else:
            ert = e

        if elso_alk or ert < legkisebb:
            legkisebb = ert
            elso_alk = False

    return legkisebb



def szamol(cel, nxs):
    """[Írj egy szamol függvényt, amely visszaadja egy cel elem el˝ofordulásának számát a beágyazott listában:]

    Args:
        lista ([type]): [description]
        cel ([type]): [description]
    """
    return kisimit(nxs).count(cel)
        


def kisimit(nxs):
    """[Írjon egy olyan kisimit függvényt, amely egy egyszer˝u listát ad vissza, amely tartalmazza az összes, a beágyazott listán szerepl˝o értéket:]

    Args:
        lista ([type]): [description]
    """
    gather = []
    for item in nxs:
        if isinstance(item, (list, tuple, set)):
            gather.extend(kisimit(item))            
        else:
            gather.append(item)
    return gather



tesztkeszlet()
