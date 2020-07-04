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
    # 7.26.1
    teszt(hany_paratlan([0,1,2,3]) == 2)
    teszt(hany_paratlan([5,5,3]) == 3)
    teszt(hany_paratlan([2,2,2]) == 0)
    # 7.26.2
    teszt(osszeg_paros([0,1,2,3]) == 2)
    teszt(osszeg_paros([2,2,2]) == 6)
    teszt(osszeg_paros([5,5,3]) == 0)
    # 7.26.3
    teszt(osszeg_neg([0,1,2,3]) == 0)
    teszt(osszeg_neg([-2,2,-2]) == -4)
    teszt(osszeg_neg([5,-5,3]) == -5)
    # 7.26.4
    teszt(hany_otbetus(["a","a","a","a"]) == 0)
    teszt(hany_otbetus(["aaaaa","a","a"]) == 1)
    teszt(hany_otbetus(["aaaaa","aaaaa","aaaaaaa"]) == 2)
    # 7.26.5
    teszt(osszeg_paroselot([0,1,2,3]) == 0)
    teszt(osszeg_paroselot([-2,2,-2]) == 0)
    teszt(osszeg_paroselot([5,-5,3,2]) == 3)
    # 7.26.6
    teszt(hany_nemig(["nem","a","a","nem","a","a"]) == 0)
    teszt(hany_nemig(["aaaaa","nem","a","a"]) == 1)
    teszt(hany_nemig(["aaaaa","aaaaa","nem","aaaaaaa"]) == 2)



# 7.26.1
def hany_paratlan(lista):
    """[Írj egy függvényt, ami megszámolja hány páratlan szám van egy listában!]

    Args:
        lista ([type]): [description]
    """
    index = 0
    for i in lista:
        if i % 2 != 0:
            index += 1
    return index

# 7.26.2
def osszeg_paros(lista):
    """[Add össze az összes páros számot a listában!]

    Args:
        lista ([type]): [description]
    """
    osszeg = 0
    for i in lista:
        if i % 2 == 0:
            osszeg += i
    return osszeg


# 7.26.3
def osszeg_neg(lista):
    """[Összegezd az összes negatív számot a listában!]

    Args:
        lista ([type]): [description]
    """
    osszeg = 0
    for i in lista:
        if i < 0:
            osszeg += i
    return osszeg


# 7.26.4
def hany_otbetus(lista):
    """[Számold meg hány darab 5 bet˝us szó van egy listában!]

    Args:
        parameter_list ([type]): [description]
    """
    index = 0
    for i in lista:
        if len(i) == 5:
            index += 1
    return index

# 7.26.5
def osszeg_paroselot(lista):
    """[Összegezd egy lista els˝o páros száma el˝otti számokat! (Írd meg az egységtesztedet! Mi van, ha nincs egyáltalán
páros szám?)]

    Args:
        parameter_list ([type]): [description]
    """
    osszeg = 0
    for i in lista:
        if i % 2 ==0:
            return osszeg
        else:
            osszeg += i
    return osszeg
    
# 7.26.6
def hany_nemig(lista):
    """[Számold meg, hány szó szerepel egy listában az els˝o „nem” szóig (beleértve magát a „nem” szót is! (Írd meg itt
is az egységtesztedet! Mi van, ha a „nem” szó egyszer sem jelenik meg a listában?)]

    Args:
        parameter_list ([type]): [description]
    """
    index = 0
    for i in lista:
        if i == "nem":
            return index
        else:
            index += 1

    return index
    

tesztkeszlet()