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
    teszt(szo_tisztitas("hogyan?") == "hogyan")
    teszt(szo_tisztitas("'most!'") == "most")
    teszt(szo_tisztitas("?+='s-z-a-v!a,k@$()'") == "szavak")
    teszt(van_duplavonal("kicsi--nagy") == True)
    teszt(van_duplavonal("") == False)
    teszt(van_duplavonal("magas--") == True)
    teszt(van_duplavonal("piros--fekete") == True)
    teszt(van_duplavonal("-igen-nem-") == False)
    teszt(szavakra_bontas(" Most van itt az id˝o? Igen, most.") == ['most','van','itt','az','id˝o','igen','most'])
    teszt(szavakra_bontas("˝O megpróbált udariasan viselkedni!") == ['˝o','megpróbált','udvariasan','viselkedni'])
    teszt(szavak_szama("most", ["most","kés˝obb","soha","most"]) == 2)
    teszt(szavak_szama("itt", ["itt","ott","amott","itt","ott","amott","itt"]) == 3)
    teszt(szavak_szama("tél", ["tavasz","nyár","˝osz","tél","tavasz","nyár","˝osz"]) == 1)
    teszt(szavak_szama("kakukk", ["cinege","fecske","gólya","sas","veréb","páva","rigó"]) == 0)
    teszt(szo_halmaz(["most", "van", "itt", "most", "van", "itt"]) == ["itt", "most", "van"])
    teszt(szo_halmaz(["én", "te", "˝o", "én", "te", "˝o", "mi", "én"]) == ["én", "mi", "˝o", "te"])
    teszt(szo_halmaz(["egy", "kett˝o", "három", "négy", "öt", "hat", "hét","nyolc"]) == ["egy", "három", "hat", "hét", "kett˝o", "négy", "nyolc", "öt"]])

    teszt(leghosszabb_szo(["alma", "eper", "körte", "sz˝ol˝o"]) == 5)
    teszt(leghosszabb_szo(["én", "te", "˝o", "mi"]) == 2)
    teszt(leghosszabb_szo(["ez","szórakoztatóelektronikai"]) == 24)
    teszt(leghosszabb_szo([ ]) == 0)

tesztkeszlet()
