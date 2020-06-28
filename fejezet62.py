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
    # 6.9.3
    teszt(nap_sorszam("péntek") == 4)
    teszt(nap_sorszam("hétfő") == 0)
    teszt(nap_sorszam(nap_nev(3)) == 3)
    teszt(nap_nev(nap_sorszam("csütörtök")) == "csütörtök")
    teszt(nap_sorszam("nap_nev(3)") == None)
    teszt(nap_sorszam("Halloween") == None)
    # 6.9.4
    teszt(napok_hozzaadasa("hétfő", 4) == "péntek")
    teszt(napok_hozzaadasa("kedd", 0) == "kedd")
    teszt(napok_hozzaadasa("kedd", 14) == "kedd")
    teszt(napok_hozzaadasa("vasárnap", 100) == "kedd")
    teszt(napok_hozzaadasa("vas", 100) == None)
    teszt(napok_hozzaadasa("vasárnap", "100") == None)
    teszt(napok_hozzaadasa("vas", "100") == None)
    # 6.9.5
    teszt(napok_hozzaadasa("vasárnap", -1) == "szombat")
    teszt(napok_hozzaadasa("vasárnap", -7) == "vasárnap")
    teszt(napok_hozzaadasa("kedd", -100) == "vasárnap")
    teszt(napok_hozzaadasa("kedd", -10) == "szombat")
    teszt(napok_hozzaadasa("kedd", -20) == "szerda")
    # 6.9.6
    teszt(honap_napja("február") == 28)
    teszt(honap_napja("november") == 30)
    teszt(honap_napja("december") == 31)
    teszt(honap_napja("Hallowen") == None)
    # 6.9.7
    teszt(masodpercre_valtas(2, 30, 10) == 9010)
    teszt(masodpercre_valtas(2, 0, 0) == 7200)
    teszt(masodpercre_valtas(0, 2, 0) == 120)
    teszt(masodpercre_valtas(0, 0, 42) == 42)
    teszt(masodpercre_valtas(0, -10, 10) == -590)
    # 6.9.8
    teszt(masodpercre_valtas(2.5, 0, 10.71) == 9010)
    teszt(masodpercre_valtas(2.433,0,0) == 8758)
    # 6.9.9
    teszt(orakra_valtas(9010) == 2)
    teszt(percekre_valtas(9010) == 30)
    teszt(masodpercekre_valtas(9010) == 10)
    # 6.9.10
    teszt(3 % 4 == 0)
    teszt(3 % 4 == 3)
    teszt(3 / 4 == 0)
    teszt(3 // 4 == 0)
    teszt(3+4 * 2 == 14)
    teszt(4-2+2 == 0)
    teszt(len("helló, világ!") == 13)
    # 6.9.11
    teszt(osszehasonlitas(5, 4) == 1)
    teszt(osszehasonlitas(7, 7) == 0)
    teszt(osszehasonlitas(2, 3) == -1)
    teszt(osszehasonlitas(42, 1) == 1)
    # 6.9.12
    teszt(atfogo(3, 4) == 5.0)
    teszt(atfogo(12, 5) == 13.0)
    teszt(atfogo(24, 7) == 25.0)
    teszt(atfogo(9, 12) == 15.0)
    # 6.9.13
    teszt(meredekseg(5, 3, 4, 2) == 1.0)
    teszt(meredekseg(1, 2, 3, 2) == 0.0)
    teszt(meredekseg(1, 2, 3, 3) == 0.5)
    teszt(meredekseg(2, 4, 1, 2) == 2.0)
    teszt(meredekseg(2, 4, 2, 5) == None)
    teszt(metszespont(1, 6, 3, 12) == 3.0)
    teszt(metszespont(6, 1, 1, 6) == 7.0)
    teszt(metszespont(4, 6, 12, 8) == 5.0)
    # 6.9.14
    teszt(paros_e(3) == False)
    teszt(paros_e(4) == True)
    teszt(paros_e("a") == None)
    teszt(paros_e(4.2) == None)
    # 6.9.15
    teszt(paratlen_e(3) == True)
    teszt(paratlen_e(4) == False)
    teszt(paratlen_e("a") == None)
    teszt(paratlen_e(4.2) == None)
    # 6.9.16
    teszt(tenyezo_e(3, 12))
    teszt(not tenyezo_e(5, 12))
    teszt(tenyezo_e(7, 14))
    teszt(not tenyezo_e(7, 15))
    teszt(tenyezo_e(1, 15))
    teszt(tenyezo_e(15, 15))
    teszt(not tenyezo_e(25, 15))
    # 6.9.17
    teszt(tobbszorose_e(12, 3))
    teszt(tobbszorose_e(12, 4))
    teszt(not tobbszorose_e(12, 5))
    teszt(tobbszorose_e(12, 6))
    teszt(not tobbszorose_e(12, 7))
    # 6.9.18
    teszt(celsiusra_valtas(212) == 100) # A víz forráspontja
    teszt(celsiusra_valtas(32) == 0) # A víz fagyáspontja
    teszt(celsiusra_valtas(-40) == -40) # Ó, micsoda érdekes eset!
    teszt(celsiusra_valtas(36) == 2)
    teszt(celsiusra_valtas(37) == 3)
    teszt(celsiusra_valtas(38) == 3)
    teszt(celsiusra_valtas(39) == 4)
    # 6.9.19
    teszt(fahrenheitre_valtas(0) == 32)
    teszt(fahrenheitre_valtas(100) == 212)
    teszt(fahrenheitre_valtas(-40) == -40)
    teszt(fahrenheitre_valtas(12) == 54)
    teszt(fahrenheitre_valtas(18) == 64)
    teszt(fahrenheitre_valtas(-48) == -54)

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
    """Írj egy nap_nev függvényt, amely a [0, 6] tartományba es˝o egész számot vár paraméterként, és visszaadja az
adott sorszámú nap nevét. A 0. nap a hétf˝o. Még egyszer leírjuk, ha nem várt érték érkezik, akkor None értékkel
térj vissza. Néhány teszt, melyen át kell mennie a függvényednek:

    Args:
        nap_szam ([int]): [description]

    Returns:
        [str]: [description]
    """
    napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
    if type(nap_szam) != int:
        return None
    elif nap_szam >= 0 and nap_szam <= 6:
        return napok[nap_szam]
    else:
        return None

# 6.9.3 feladat
def nap_sorszam(nap):
    """[Írd meg az el˝oz˝o függvény fordítottját, amely egy nap neve alapján adja meg annak sorszámát:]

    Args:
        nap ([type]): [description]
    """

    napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
    
    for i in range(7):
        if napok[i] == nap:
            return i
    
    return None

# 6.9.4 feladat + 6.9.5
def napok_hozzaadasa(nap, napok_szama):
    """[Írj egy függvényt, amely segít megválaszolni az ehhez hasonló kérdéseket: „Szerda van. 19 nap múlva nyaralni
megyek. Milyen napra fog esni?” A függvénynek tehát egy nap nevét és egy „hány nap múlva” értéket vár
argumentumként, és egy nap nevét adja vissza:]

    Args:
        nap ([type]): [description]
        napok_szama ([type]): [description]

    Returns:
        [type]: [description]
    """
    if nap_sorszam(nap) == None:
        return None
    
    if type(napok_szama) != int:
        return None

    if nap_sorszam(nap) + napok_szama >= 0:
        return (nap_nev(abs(((nap_sorszam(nap) + napok_szama) % 7)) % 6))
    else:
        return nap_nev((nap_sorszam(nap) + napok_szama)%7)
    

# 6.9.6
def honap_napja(honap):
    """[Írj egy honap_napja függvényt, mely egy hónap neve alapján megadja, hogy hány nap van a hónapban. (A
szök˝oévekkel ne foglalkozz.):]
    """
    if type(honap) != str:
        return None

    honapok = {"január" : 31, "február" : 28, "március":31,"április":30,"május":31,"június":30,"július":31,"augusztus":31,"szeptember":30,"október":31, "november":30, "december":31}

    try:
        return honapok[honap]
    except:
        pass
    
# 6.9.7 + 6.9.8
def masodpercre_valtas(hh, mm, ss):
    """[Írj egy masodpercre_valtas függvényt, mely órákat, perceket és másodperceket kap meg argumentumként,
és kiszámolja hány másodpercnek felelnek meg összesen. Néhány teszteset:]

    Args:
        hh ([int]): [description]
        mm ([int]): [description]
        ss ([int]): [description]
    """
    if not(isinstance(hh, int)) and not(isinstance(hh, float)):
        return None
    elif not(isinstance(mm, int)) and not(isinstance(mm, float)):
        return None
    elif not(isinstance(ss, int)) and not(isinstance(ss, float)):
        return None
    
    return int((hh * 3600) + (mm * 60) + ss)

# 6.9.9
# A
def orakra_valtas(ss):
    """[orakra_valtas: az argumentumként átadott másodperceket órákra váltja. A teljes órák számával tér
vissza.]

    Args:
        ss ([type]): [description]
    """
    return ss // 3600
    
# B
def percekre_valtas(ss):
    """[percekre_valtas: az argumentumként átadott másodpercekb˝ol leszámítja a teljes órákat, a maradékot
pedig percekbe váltja. A teljes percek számával tér vissza.]

    Args:
        ss ([type]): [description]
    """
    return (ss%3600) // 60
# C
def masodpercekre_valtas(ss):
    """[masodpercekre_valtas: visszatér az argumentumként kapott másodpercekb˝ol fennmaradó másodpercekkel.]

    Args:
        ss ([type]): [description]
    """
    return (ss % 3600)%60

# 6.9.11
def osszehasonlitas(a, b):
    """[Írj egy osszehasonlitas függvényt, amely 1-et ad vissza, ha a > b, 0-t ad vissza, ha a == b, és -1-t,
ha a < b]

    Args:
        a ([type]): [description]
        b ([type]): [description]
    """
    if a > b:
        return 1
    elif a==b:
        return 0
    else:
        return -1

# 6.9.12
def atfogo(a, b):
    """[Írj egy atfogo nev˝u függvényt, amely egy derékszög˝u háromszög két befogójának hossza alapján visszaadja
az átfogó hosszát:]

    Args:
        a ([type]): [description]
        b ([type]): [description]
    """
    return (a**2 + b**2)**(1/2)

# 6.9.13
# A
def meredekseg(x1, y1, x2, y2):
    """[Implementáld a meredekseg(x1, y1, x2, y2) függvényt, úgy, hogy az (x1, y1) és (x2, y2) pontokon
átmen˝o egyenes meredekségét határozza meg:]

    Args:
        x1 ([type]): [description]
        y1 ([type]): [description]
        x2 ([type]): [description]
        y2 ([type]): [description]
    """
    try:
        return (y2-y1)/(x2-x1)
    except:
        return None

# B
def metszespont(x1, y1, x2, y2):
    """[Utána használd fel egy új, metszespont(x1, y1, x2, y2) függvényben, amely visszaadja, hogy az
(x1, y1), (x2, y2) pontokon átmen˝o egyenes milyen y értéknél metszi a derékszög˝u koordinátarendszer
függ˝oleges tengelyét. (Feltételezheted, hogy az x1 és x2 értéke különböz˝o.):]

    Args:
        x1 ([type]): [description]
        y1 ([type]): [description]
        x2 ([type]): [description]
        y2 ([type]): [description]
    """
    m = meredekseg(x1, y1, x2, y2)
    return y1 - m * x1    

# 6.9.14
def paros_e(n):
    """[Írj egy paros_e(n) függvényt, amely egy egészet vár argumentumként, és True-t ad vissza, ha az argumentum
páros szám, és False-t, ha páratlan]

    Args:
        n ([type]): [description]
    """
    if not(isinstance(n, int)):
        return None

    if n % 2 == 0:
        return True
    else:
        return False
    
# 6.9.15
def paratlen_e(n):
    """[Most írj egy paratlen_e(n) függvényt is, amely akkor tér vissza True értékkel, ha n páratlan, és akkor
False értékkel, ha páros. Teszteket is készíts!]

    Args:
        n ([type]): [description]
    """
    if paros_e(n) == None:
        return None

    return not paros_e(n)

 # 6.9.16
def tenyezo_e(t, n):
    """[Készíts egy tenyezo_e(t, n) fejléc˝u függvényt, amely átmegy az alábbi teszteken. (Ne csak a prímtényez
˝okre adjon vissza igazat a függvényed.):]

     Args:
         t ([type]): [description]
         n ([type]): [description]
    """
    return n % t == 0

# 6.9.17
def tobbszorose_e(n, t):
    """[Írj egy tobbszorose_e fejléc˝u függvényt, mely kielégíti az alábbi egységtesztet:]

    Args:
        t ([type]): [description]
        n ([type]): [description]
    """
    return n % t == 0
    
# 6.9.18
def celsiusra_valtas(f):
    """[Írj egy celsiusra_valtas(f) függvényt, mely egy Fahrenheitben megadott értéket Celsius fokra vált át.
A függvény a legközelebbi egész értéket adja vissza. (Segítség: Ha a beépített round függvényt szeretnéd
használni, próbáld kiíratni a round.__doc__ -et a Python konzolban, vagy a függvény nevén állva nyomd le
a Ctrl+Q billenty˝ukombinációt. Kísérletezz, ameddig rá nem jössz, hogyan m˝uködik. ):]

    Args:
        f ([type]): [description]
    """
   
    return round((f - 32) * (5/9))

# 6.9.19
def fahrenheitre_valtas(c):
    """[Most tedd az ellenkez˝ojét: írj egy celsiusra_valtas függvényt, mely egy Celsius-fokban megadott értéket
Fahrenheit skálára vált át:]

    Args:
        c ([type]): [description]
    """
    return round(c * (9/5) + 32)
    

# Tesztvegrehajtasa
tesztkeszlet()