import sys
import math

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
    p = Pont(-5, 3)
    q = Pont(4, -2)
    teszt(p.tavolsag(q) - math.sqrt(196) <= 0.00000001)
    # sulypont_szamitas
    teszt(Pont(0,1).sulypont_szamitas(Pont(7,2)) == Pont(7/2, 3/2))
    teszt(Pont(7,2).sulypont_szamitas(Pont(9,-2)) == Pont(8, 0))
    # tukrozes_x_tengelyre
    teszt(p.tukrozes_x_tengelyre() == Pont(-5, -3))
    teszt(q.tukrozes_x_tengelyre() == Pont(4, 2))
    # origotol_mert_meredekseg
    teszt(p.origotol_mert_meredekseg() == (3/-5) )
    teszt(q.origotol_mert_meredekseg() == (-2/4) )
    # egyenes
    teszt(Pont(4, 11).egyenes(Pont(6, 15)) == (2, 3) )
    teszt(Pont(3, 5).egyenes(Pont(5, 2)) == (-1.5, 19/2) )
    # ketpont_vector
    teszt(Pont(7, 2).ketpont_vector(Pont(0, 1)) == (7, 1) )
    teszt(Pont(9, -2).ketpont_vector(Pont(7, 2)) == (2, -4) )
    # egyenes_meroleges
    teszt(Pont(7, 2).egyenes_meroleges(Pont(0, 1)) == (7, 1, 26) )
    teszt(Pont(9, -2).egyenes_meroleges(Pont(7, 2)) == (2, -4, 16) )
    # kor_harompontbol
    teszt(Pont(-3, 1).kor_harompontbol(Pont(1, -7), Pont(6, -2)) == Pont(1, -2) )
    teszt(Pont(0, 1).kor_harompontbol(Pont(7, 2), Pont(9, -2)) == Pont(4, -2) )
    # pont_kerekit_egyezik
    teszt(Pont(4, 11).pont_kerekit_egyezik(Pont(3.9999999999999, 11.00000000001)) == True )
    teszt(Pont(4, 11).pont_kerekit_egyezik(Pont(5, 11.00000000001)) == False )
    # kor_negypontbol
    teszt(Pont(1, 0).kor_negypontbol(Pont(0, 1), Pont(-1, 0), Pont(0, -1)) == Pont(0, 0) )
    teszt(Pont(-3, 1).kor_negypontbol(Pont(1, -7), Pont(6, -2), Pont(0, ((-4)+math.sqrt(96)) / 2 )) == Pont(1, -2) )


class Pont:
    """[Pont osztály (x, y) koordináták reprezentálására és manipulálására]
    """
    def __init__(self, x=0, y=0):
        """[Egy új, x, y koordinátán álló pont készítése]

        Args:
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
        """
        self.x = x
        self.y = y
    
    def __eq__(self, other): 
        if not isinstance(other, Pont):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def origotol_mert_tavolsag(self):
        """[Az origótól mért távolság számítása]
        """
        return ((self.x**2) + (self.y**2))**0.5

    def sztringge_alakitas(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self):  # A metódus átnevezése az egyetlen feladatunk
        return "({0}, {1})".format(self.x, self.y)

    def sulypont_szamitas(self, masik_pont):
        """[A súlypontom a másik ponttal]

        Args:
            masik_pont ([type]): [description]
        """
        mx = (self.x + masik_pont.x) / 2
        my = (self.y + masik_pont.y) / 2
        return Pont(mx, my)

    def tavolsag(self, masik_pont):
        """[Írd át a Produktív függvények fejezetben található tavolsag függvényt úgy, hogy négy szám típusú paraméter helyett két Pont típusú paramétere legyen!]
        """
        return ((self.x**2-masik_pont.x**2) + (self.y**2-masik_pont.y**2))**0.5

    def tukrozes_x_tengelyre(self):
        """[B˝ovítsd egy tukrozes_x_tengelyre nev˝u metódussal a Pont osztályt! A metódus térjen vissza egy új Pont példánnyal, mely az aktuális pont x-tengelyre vett tükörképe. Például a Pont(3, 5). tukrozes_x_tengelyre() eredménye (3, -5).]
        """
        new_x = self.x
        new_y = -1 * self.y
        return Pont(new_x, new_y)

    def origotol_mert_meredekseg(self):
        """[Adj hozzá az osztályhoz egy origotol_mert_meredekseg nev˝u metódust, amely az origó és a pont közti egyenes szakasz meredekségét határozza meg! A Pont(4, 10).origotol_mert_meredekseg() eredménye például 2.5.]
        """
        return self.y/self.x

    def egyenes(self, masik_pont):
        """[Az egyenes egyenlete y = ax + b (vagy másképpen y = mx + c). Az a és b együtthatók egyértelm˝uen meghatározzák az egyenest. Írj egy metódust a Pont osztályon belül, amely az aktuális objektum és egy másik, argumentumként kapott pont alapján meghatározza a két ponton átmen˝o egyenest! A metódusnak az egyenes együtthatóival, mint értékpárral, kell visszatérniük:]

        Args:
            masik_pont ([type]): [description]
        """
        a = (self.y - masik_pont.y)/(self.x - masik_pont.x)
        b = a * (-self.x) + self.y 
        return (a, b)

    def ketpont_vector(self, masik_pont):
        """[Ket pontra nezo meroleges fevektor]

        Args:
            masik_pont ([type]): [description]
        """
        return (self.x - masik_pont.x, self.y - masik_pont.y)

    def egyenes_meroleges(self, masik_pont):
        """[Meroleges egyenes az AB fektorra a felezeponton keresztul]

        Args:
            masik_pont ([type]): [description]
        """
        # Felezo pont
        felezo_pont = masik_pont.sulypont_szamitas(self)
        # Vektor
        vektor = self.ketpont_vector(masik_pont)
        # egyenlet parameterek
        a = vektor[0]
        b = vektor[1]
        c = a * felezo_pont.x + b * felezo_pont.y
        return (a, b, c)

    def kor_harompontbol(self, egyes_pont, kettes_pont):
        """[Kor egyenlete es kozep pontja harom pont alapjan]

        Args:
            egyes_pont ([type]): [description]
            kettes_pont ([type]): [description]
        """
        eq1 = self.egyenes_meroleges(egyes_pont)
        eq2 = egyes_pont.egyenes_meroleges(kettes_pont)
        x = (eq2[1] * eq1[2] - eq1[1] * eq2[2])/(eq1[0] * eq2[1] - eq2[0] * eq1[1])
        y = (eq1[0] * eq2[2] - eq2[0] * eq1[2])/(eq1[0] * eq2[1] - eq2[0] * eq1[1])
        return Pont(x, y)
        
    def pont_kerekit_egyezik(self, masik_pont):
        """[Ket pont kerekitve egyezik]

        Args:
            masik_pont ([type]): [description]
        """
        if abs(self.x - masik_pont.x) >= 0.000001:
            return False
        elif abs(self.y - masik_pont.y) >= 0.000001:
            return False
        else:
            return True
        

    
    def kor_negypontbol(self, egyes_pont, kettes_pont, harmas_pont):
        """[Határozd meg egy kör középpontját négy, a kör kerületére es˝o pont alapján! Milyen esetben nem fog m˝uködni a függvény? Segítség: Tudnod kell, hogyan old meg a geometriai problémát, miel˝ott a gondolataid a programozás körül kezdenének forogni. Nem tudod leprogramozni a megoldást, ameddig nem érted, hogy mit akarsz a géppel megcsináltatni]

        Args:
            egyes_pont ([type]): [description]
            kettes_pont ([type]): [description]
            harmas_pont ([type]): [description]
        """
        p1 = self.kor_harompontbol(egyes_pont, kettes_pont) 
        p2 = self.kor_harompontbol(kettes_pont, harmas_pont)
        p3 = egyes_pont.kor_harompontbol(kettes_pont, harmas_pont)

        
        if p1.pont_kerekit_egyezik(p2) and p1.pont_kerekit_egyezik(p3) and p2.pont_kerekit_egyezik(p3):
            return p1
        else:
            None
        


tesztkeszlet()

