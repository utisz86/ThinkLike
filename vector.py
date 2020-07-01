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
    # 11.22.5
    teszt(vektorok_osszege([1, 1], [1, 1]) == [2, 2])
    teszt(vektorok_osszege([1, 2], [1, 4]) == [2, 6])
    teszt(vektorok_osszege([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    # 11.22.6
    teszt(szorzas_skalarral(5, [1, 2]) == [5, 10])
    teszt(szorzas_skalarral(3, [1, 0, -1]) == [3, 0, -3])
    teszt(szorzas_skalarral(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    # 11.22.7
    teszt(skalaris_szorzat([1, 1], [1, 1]) == 2)
    teszt(skalaris_szorzat([1, 2], [1, 4]) == 9)
    teszt(skalaris_szorzat([1, 2, 1], [1, 4, 3]) == 12)
    # 11.22.8
    teszt(vektorialis_szorzat([1, 1, 1], [1, 1, 1]) == [[1, 1, 1],[1, 1, 1],[1, 1, 1]])
    teszt(vektorialis_szorzat([1, 2, 3], [1, 2, 3]) == [[1, 2, 3],[2, 4, 6],[3, 6, 9]])
    teszt(vektorialis_szorzat([0, 1, 0], [1, 0, 1]) == [[0, 0, 0],[1, 0, 1],[0, 0, 0]])

# 11.22.5
def vektorok_osszege(u, v):
    """[A listákat használhatjuk matematikai vektorok ábrázolására. Ebben és az ezt követ˝o néhány gyakorlatban olyan
függvényeket írunk le, amelyek végrehajtják a vektorok alapvet˝o m˝uveleteit. Hozz létre egy vectorok.py
szkriptet, és írd bele az alábbi Python kódot, hogy mindegyiket letesztelhesd!
Írj egy vektorok_osszege(u, v) függvényt, amely paraméterként két azonos hosszúságú listát kap, és
adjon vissza egy új listát, mely tartalmazza a megfelel˝o elemek összegét:]

    Args:
        u ([type]): [description]
        v ([type]): [description]
    """
    uj_vetor = []
    for (i, elem) in enumerate(u):
        uj_vetor.append(elem + v[i])
    
    return uj_vetor

# 11.22.6
def szorzas_skalarral(s, v):
    """[Írj egy szorzas_skalarral(s, v) függvényt, amely paraméterként egy s számot, és egy v listát kap, és
visszatér a függvény a v lista s skalárral való szorzatával.]

    Args:
        s ([type]): [description]
        v ([type]): [description]
    """
    uj_vetor = []
    for elem in v:
        uj_vetor.append(s*elem)
    return uj_vetor

# 11.22.7
def skalaris_szorzat(u, v):
    """[Írj egy skalaris_szorzat(u, v) függvényt, amely paraméterként megkap két azonos hosszúságú számokat
tartalmazó listát, és visszaadja a megfelel˝o elemek skaláris szorzatát.]

    Args:
        u ([type]): [description]
        v ([type]): [description]
    """
    uj_vetor = 0
    for (i, elem) in enumerate(u):
        uj_vetor += (elem * v[i])
    
    return uj_vetor

# 11.22.8
def vektorialis_szorzat(u, v):
    """[Extra matematikai kihívások: Írj egy vektorialis_szorzat(u, v) függvényt, amely paraméterként
megkap két 3 hosszúságú számokból álló listát, és visszatér a vektoriális szorzatukkal. Írd meg a saját tesztjeid]

    Args:
        u ([type]): [description]
        v ([type]): [description]
    """
    uj_lista = []
    uj_sor = []
    for u_elem in u:
        for v_elem in v:
            uj_sor.append(u_elem * v_elem)
        uj_lista.append(uj_sor)
        uj_sor = []
    return uj_lista


tesztkeszlet()
