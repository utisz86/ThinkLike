import sys
import random

szelvenyek = [ [ 7, 17, 37, 19, 23, 43],
               [ 7, 2, 13, 41, 31, 43],
               [ 2, 5, 7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

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
    # A
    teszt(len(lottohuzas()) == 5)
    teszt(max(lottohuzas()) <= 49)
    teszt(min(lottohuzas()) >= 1)
    # B
    teszt(lotto_talalat([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
    # C
    szelvenyek = [ [ 7, 17, 37, 19, 23, 43],
               [ 7, 2, 13, 41, 31, 43],
               [ 2, 5, 7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]
    teszt(lotto_talalatok([42,4,7,11,1,13], szelvenyek) == [1,2,3,1])
    # D
    teszt(primek_szama([42, 4, 7, 11, 1, 13]) == 3)
    teszt(is_prime(7) == True)
    teszt(is_prime(2) == True)
    teszt(is_prime(8) == False)
    # E
    teszt(hianyzo_primek(szelvenyek) == [3, 29, 47])
    # F
    teszt(uj_huzasok(szelvenyek, seed = 1) == [0, 0, 0, 0])
    teszt(uj_huzasok(szelvenyek, seed = 2) == [1, 1, 1, 0])
    


def lottohuzas(seed=1):
    """[Minden lottószelvény húzáshoz hat véletlenszer˝u golyó tartozik, sorszámozva 1-t˝ol 49-ig. Írj egy függvényt, mely visszatér egy lottóhúzással.]

    Args:
        args ([type]): [description]
    """
    rng = random.Random(seed)   # A generátor létrehozása
    bd = list(range(1,50))
    rng.shuffle(bd)
    return bd[0:5]
    
def lotto_talalat(szelveny, huzas):
    """[Írj egy függvényt, amely összehasonlít egy egyszer˝u szelvényt és egy lottóhúzást, visszaadja a találtok számát:]

    Args:
        parameter_list ([type]): [description]
    """
    talalat = 0
    for i in szelveny:
        if i in huzas:
            talalat += 1
    return talalat

def lotto_talalatok(huzas, szelvenyek):
    """[Írj egy függvényt, amely megkapja a szelvények és húzások listáját, és visszatér egy olyan listával, mely megadja, hogy minden egyes szelvényen hány találat volt:]

    Args:
        parameter_list ([type]): [description]
    """
    talalat = []
    for szelveny in szelvenyek:
        talalat.append(lotto_talalat(szelveny, huzas))
    return talalat

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6. 
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True    

def primek_szama(lista):
    """[(d) Írj egy függvényt, amely megkapja az egész számok listáját, és visszatér a listában szerepl˝o prímszámok számával:]

    Args:
        args ([type]): [description]
    """
    eredmenyenek = 0
    for e in lista:
        if is_prime(e):
            eredmenyenek += 1
    return eredmenyenek


def hianyzo_primek(szelvenyek):
    """[Írj egy függvényt, amely felderíti, hogy vajon az informatikus elhibázott-e prímszámokat a négy szelvényén.
Térjen vissza a prímszámok listájával, amelyeket elhibázott:]

    Args:
        szelvenyek ([type]): [description]
    """
    prim = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    flat_list = []
    for sublist in szelvenyek:
        for item in sublist:
            flat_list.append(item)
    
    szelvenyek = list(set(flat_list))
    eredmeny = []
    for i in prim:
        if i not in szelvenyek:
            eredmeny.append(i)
    return eredmeny

def uj_huzasok(szelvenyek, seed = 1):   
    """[Írj egy függvényt, amely ismételten új húzást generál, és összehasonlítja a húzásokat a négy szelvénnyel!]

    Args:
         szelvenyek ([type]): [description]
    """
    return lotto_talalatok(lottohuzas(seed), szelvenyek)


# Python program to get average of a list 
def Average(lst): 
    return sum(lst) / len(lst)     
    

tesztkeszlet()

"""[Számold meg hány húzás szükséges addig, amíg az informatikus szelvényein legkevesebb három
találatost kap! Próbáld ki a kísérletet hússzor, és átlagold a szükséges húzások számát!]
"""

huzasok_szama_list = []
for i in range(20):
    huzasok_szama = 0
    while True:
        if max(uj_huzasok(szelvenyek, seed = random.randint(0,10000))) >= 3:
            huzasok_szama_list.append(huzasok_szama)
            break
        huzasok_szama += 1
print("Huzasok min 3: {0}, Atlag: {1}".format(huzasok_szama_list, Average(huzasok_szama_list) ))

huzasok_szama_list = []
for i in range(20):
    huzasok_szama = 0
    while True:
        if max(uj_huzasok(szelvenyek, seed = random.randint(0,10000))) >= 4:
            huzasok_szama_list.append(huzasok_szama)
            break
        huzasok_szama += 1
print("Huzasok min 4: {0}, Atlag: {1}".format(huzasok_szama_list, Average(huzasok_szama_list) ))


huzasok_szama_list = []
for i in range(20):
    huzasok_szama = 0
    while True:
        if max(uj_huzasok(szelvenyek, seed = random.randint(0,10000))) >= 5:
            huzasok_szama_list.append(huzasok_szama)
            break
        huzasok_szama += 1
print("Huzasok min 5: {0}, Atlag: {1}".format(huzasok_szama_list, Average(huzasok_szama_list) ))

