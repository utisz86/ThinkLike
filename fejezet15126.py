import sys
from time import gmtime, strftime

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
    # Extra tesztek
    bejovo_uzenetek = SMS_tarolo()
    teszt(isinstance(bejovo_uzenetek, SMS_tarolo))
    # SMS hozza adasa
    bejovo_uzenetek.beerkezo_uzenet_hozzaadasa("1234", "12:35", "Hello world 1!")
    bejovo_uzenetek.beerkezo_uzenet_hozzaadasa("1234", "12:36", "Hello world 2!")
    bejovo_uzenetek.beerkezo_uzenet_hozzaadasa("1234", "12:37", "Hello world 3!")
    bejovo_uzenetek.beerkezo_uzenet_hozzaadasa("1234", "12:38", "Hello world 4!")
    teszt(len(bejovo_uzenetek.uzenetek) == 4)
    # bejovo_uzenetek.uzenetek_szama()
    teszt(bejovo_uzenetek.uzenetek_szama() == 4)
    # olvasatlan_uzenetek_indexeinek_lekerese() A
    bejovo_uzenetek.uzenetek.append(("True","1234", "12:38", "Hello world 4!"))
    teszt(bejovo_uzenetek.olvasatlan_uzenetek_indexeinek_lekerese() == list(range(4)))
    # uzenet_lekerese(i)
    teszt( bejovo_uzenetek.uzenet_lekerese(0) == ('True', '1234', '12:35', 'Hello world 1!'))
    teszt( bejovo_uzenetek.uzenet_lekerese(4) == ('True', '1234', '12:38', 'Hello world 4!'))
    teszt( bejovo_uzenetek.uzenet_lekerese(5) == None)
    # olvasatlan_uzenetek_indexeinek_lekerese() B
    teszt(bejovo_uzenetek.olvasatlan_uzenetek_indexeinek_lekerese() == [1,2,3])
    # torol(i)
    bejovo_uzenetek.torol(0)
    teszt( len(bejovo_uzenetek.uzenetek) == 4)
    # mindent_torol()
    bejovo_uzenetek.mindent_torol()
    teszt( bejovo_uzenetek.uzenetek == [])

class SMS_tarolo:
    """[Készíts egy új SMS_tarolo osztályt! Az osztály olyan objektumokat példányosít majd, amelyek hasonlítanak a telefonon lév˝o bejöv˝o / kimen˝o üzenet tárolókra:]

    Args:
        object ([type]): [description]
    """
    def __init__(self, uzenetek = []):
        self.uzenetek = uzenetek

    def beerkezo_uzenet_hozzaadasa(self, kuldo_szama, erkezesi_ido, SMS_szovege):
        """[Készít egy új rendezett 4-est az SMS számára,
            és beszúrja ˝oket a tárolóba a többi üzenet után.
            Az üzenet készítésénél az olvasott_e állapotát
            hamisra (False) állítja.]
        """
        self.uzenetek.append(('False',kuldo_szama, erkezesi_ido, SMS_szovege))

    def uzenetek_szama(self):
        """[Visszatér a bejovo_uzenetek tárolóban lév˝o SMS-ek számával]
        """
        return len(self.uzenetek)

    def olvasatlan_uzenetek_indexeinek_lekerese(self):
        """[Visszatér az összes olvasatlan SMS indexét tartalmazó listával.]
        """
        eredmeny = []
        for (i, uzenet) in enumerate(self.uzenetek):
            if uzenet[0] == 'False':
                eredmeny.append(i)
        return eredmeny
        
    def uzenet_lekerese(self, i):
        """[Visszatér az uzenet[i]-hez tartozó (kuldo_szama, erkezesi_ido, SMS_szovege) 4- essel. Az üzenet státuszát olvasottra állítja. Ha nincs üzenet az i. indexen, akkor a visszatérési érték None.]

        Args:
            i ([type]): [description]
        """
        try:
            result = self.uzenetek[i]
            result = ('True',result[1], result[2], result[3])
            self.uzenetek[i] = result
        except:
            result =  None

        return result
        

    def torol(self, i):
        """[Kitörli az i. pozícióban álló üzenetet.]

        Args:
            i ([type]): [description]
        """
        del self.uzenetek[i]

    def mindent_torol(self):
        """[Kitörli az összes üzenetet a bejöv˝o SMS-ek tárolójából.]
        """
        del self.uzenetek[:]
        



tesztkeszlet()


