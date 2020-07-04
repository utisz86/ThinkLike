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
    # 8.19.1
    # 8.19.2
    # 8.19.3
    teszt(karakter_szamlalas("banán", "a") == 1)
    # 8.19.4
    # 8.19.5
    teszt(eltav_irasjel("szövegben, melyből") == "szovegben, melybol")
    # 8.19.6
    # 8.19.7
    teszt(sztring_forditas("boldog") == "godlob")
    teszt(sztring_forditas("Python") == "nohtyP")
    teszt(sztring_forditas("") == "")
    teszt(sztring_forditas("a") == "a")
    # 8.19.8
    teszt(tukor("jo") == "jooj")
    teszt(tukor("Python") == "PythonnohtyP")
    teszt(tukor("") == "")
    teszt(tukor("a") == "aa")
    # 8.19.9
    teszt(betu_eltuntetes("a", "alma") == "lm")
    teszt(betu_eltuntetes("a", "banán") == "bnán")
    teszt(betu_eltuntetes("z", "banán") == "banán")
    teszt(betu_eltuntetes("e", "Kerepes") == "Krps")
    teszt(betu_eltuntetes("b", "") == "")
    teszt(betu_eltuntetes("b", "c") == "c")
    # 8.19.10
    teszt(palindrom_e("abba"))
    teszt(not palindrom_e("abab"))
    teszt(palindrom_e("teret"))
    teszt(not palindrom_e("banán"))
    teszt(palindrom_e("mesék késem"))
    teszt(palindrom_e("a"))
    # teszt(palindrom_e("")) # Egy üres sztring palindrom-e?

    # 8.19.11
    teszt(szamlalas("gö", "görögös") == 2)
    teszt(szamlalas("pa", "papaja") == 2)
    teszt(szamlalas("apa", "papaja") == 1)
    teszt(szamlalas("papa", "papaja") == 1)
    teszt(szamlalas("apap", "papaja") == 0)
    teszt(szamlalas("aaa", "aaaaaa") == 4)
    # 8.19.12
    teszt(torles("alma", "almafa") == "fa")
    teszt(torles("an", "banán") == "bán")
    teszt(torles("pa", "papaja") == "paja")
    teszt(torles("pa", "Papaja") == "Paja")
    teszt(torles("alma", "kerékpár") == "kerékpár")

    # 8.19.13
    teszt(alapos_torles("an", "banán") == "bán")
    teszt(alapos_torles("pa", "papaja") == "ja")
    teszt(alapos_torles("pa", "Papaja") == "Paja")
    teszt(alapos_torles("alma", "kerékpár") == "kerékpár")
    # A megoldástól függ˝oen: "pa" vagy ""
    teszt(alapos_torles("pa", "ppapaa" ) == "")


# 8.19.1
for i in ["Python"[1], "A sztringek karaktersorozatok."[5], len("csodálatos"), "Rejtély"[:4], "k" in "Körte",
"barack" in "sárgabarack", "körte" not in "Ananász", "barack" > "sárgabarack", "ananász" < "Barack"]:
    print(i)
# 8.19.2
elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur", "szakáll"]

for utotag in utotagok_listaja:
    print((elotag + utotag).replace("pp","p"))

# 8.19.3
def karakter_szamlalas(gyumolcs, betu):
    darab = 0
    for karakter in gyumolcs:
        if karakter == betu:
            darab += 1
    return darab

print(karakter_szamlalas("banán", "a"))
# 8.19.4
# 8.19.5
szoveg_basic = """Egy kolléga és barát, Peter Warren egyszer azt a megjegyzést tette, hogy a bevezet˝o programozás tanulása ugyanúgy szól a környezetr˝ol, mint a programnyelvr˝ol. Nagy rajongója vagyok az IDE-knek (Integrated Development Environments). Szeretem, ha a segítség bele van integrálva a szerkeszt˝ombe – mint egy olyan egyed, amely támogatja más entitások számára az általánosan elérhet˝o m˝uveleteket – amit egy gombnyomással elérhetek. Szintaxis kiemelést akarok. Szeretnék azonnali szintaxis-ellen˝orzést és jól m˝uköd˝o automatikus kiegészítést. Szeretnék egy olyan szerkeszt˝ot, amely el tudja rejteni a függvények testét vagy kódját, mert ezáltal el˝osegíti és ösztönzi a mentális absztrakciók építését. Különösen rajongok az egyszer˝u lépésenkénti hibakeres˝oért és a töréspontokért a beépített kódellen˝orzésnél. A program végrehajtásának koncepcionális modelljét próbáljuk kiépíteni a hallgató elméjében, melynek tanításához azt tartom a legjobb megoldásnak, ha a hívási vermet és a változókat láthatóvá tesszük, hogy azonnal ellen˝orizni tudjuk az utasítások végrehajtásának eredményét. Az én filozófiám tehát nem az, hogy egy olyan nyelvet keressek, amit megtaníthatok, hanem az IDE és a nyelv kombinációját keressem, amely egy csomagban van és egy egészként értékelhet˝o. Nagy változtatásokat hajtottam végre az eredeti könyvön, hogy ezt (és sok más általam is osztott véleményt) tükrözzem, és kétségem sincs afel˝ol, hogy a kurzusaink tapasztalatai lapján ezt további változások fogják követni. Íme néhány olyan kulcsfontosságú dolog, amelyet másképp közelítettem meg:
"""

def eltav_irasjel(szoveg):
    """[Írj egy függvényt, amely eltávolítja az összes írásjelet a sztringb˝ol, és a szöveget szavak listájára bontja.]

    Args:
        szoveg ([type]): [description]
    """
    pass

szavak_szama = len(szoveg_basic.split())

def kereses2(szoveg, k, kezdet):
    i = kezdet
    while i < len(szoveg):
        if szoveg[i] == k:
            return i
        i += 1
    return -1

e_betuk = kereses2(szoveg_basic, "e", 0)
e_arany = e_betuk / len(szoveg_basic)

print("A szövegben {0} szó áll, melyből {1} ({2:.2%}) tartalmaz 'e' betut.".format(szavak_szama, e_betuk, e_arany))

# 8.19.6
def szorzotabla(n):
    n +=1
    print("", end="\t")
    for i in range(1,n):
        print(i, end="\t")
    print()        
    print(" :",end="-----")
    for i in range(0, n):
        print("-------", end="")
    print()
    for i in range(1, n):
        print("{0}:".format(i), end="\t")
        for j in range(1, n):
            print(i*j, end="\t")
        print()


szorzotabla(10)
# 8.19.7
def sztring_forditas(szoveg):
    """[Írj egy függvényt, amely meghatározza egy paraméterként kapott sztring fordítottját. A függvénynek át kell
mennie ezeken a teszteken:]

    Args:
        szoveg ([type]): [description]
    """
    forditot = ""
    for i in szoveg:
        forditot = i + forditot
    return forditot
    
# 8.19.8
def tukor(szoveg):
    """[Írj egy függvényt, amely összef˝uzi argumentumát annak tükörképével:]

    Args:
        szoveg ([type]): [description]
    """
    return szoveg + sztring_forditas(szoveg)

# 8.19.9
def betu_eltuntetes(betu, szoveg):
    """[Írj függvényt, amely eltávolítja egy karakter összes el˝ofordulását egy sztringb˝ol. A függvény a karaktert és a
sztringet is argumentumként várja.]

    Args:
        betu ([type]): [description]
        szoveg ([type]): [description]
    """
    hianyos = ""
    for i in szoveg:
        if i != betu:
            hianyos += i
    return hianyos

# 8.19.10
def palindrom_e(szoveg):
    """[Írj függvényt, mely képes a palindromok felismerésére. (Segítség: a korábban megírt sztring_forditas
függvény felhasználása megkönnyíti a dolgod!):]

    Args:
        szoveg ([type]): [description]
    """
    return sztring_forditas(szoveg) == szoveg
    
# 8.19.11
def szamlalas(szoveg1, szoveg2):
    """[Írj egy függvényt, amely meghatározza, hányszor szerepel egy sztringben egy másik sztring:]

    Args:
        szoveg ([type]): [description]
    """
    index = 0
    start_i=0
    end_i=len(szoveg1)
    while True:
        if szoveg1 in szoveg2[start_i:end_i]:
            index += 1
        start_i += 1
        end_i += 1
        if end_i > (len(szoveg2) + 1):
            return index

# 8.19.12
def torles(szoveg1, szoveg2):
    """[Írj függvényt, amely eltávolítja egy sztringb˝ol egy másik sztring els˝o el˝ofordulását:]

    Args:
        szoveg1 ([type]): [description]
        szoveg2 ([type]): [description]
    """
    torolt = ""
    start_i=0
    end_i=len(szoveg1)
    while True:
        try:
            if szoveg1 == szoveg2[start_i:end_i]:
                return torolt + szoveg2[(end_i):]
            torolt += szoveg2[start_i]
            start_i += 1
            end_i += 1
        except:
            return torolt

    
# 8.19.13
def alapos_torles(szoveg1, szoveg2):
    """[Írj függvényt, amely eltávolítja egy sztringb˝ol egy másik sztring minden el˝ofordulását. (A törlés hatására új
el˝ofordulások is keletkezhetnek. Rád bízzuk, hogy ezeket elt˝unteted-e.):]

    Args:
        szoveg1 ([type]): [description]
        szoveg2 ([type]): [description]
    """
    torolt = szoveg2
    while szoveg1 in torolt:
        torolt = torolt.replace(szoveg1, "")
    
    return torolt

tesztkeszlet()
