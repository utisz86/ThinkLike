import sys
import math
from fejezet157pont import Pont 

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
    # terulet
    r = Teglalap(Pont(0, 0), 10, 5)
    teszt(r.terulet() == 50)
    # kerulet
    r = Teglalap(Pont(0, 0), 10, 5)
    teszt(r.kerulet() == 30)
    # forditas
    r = Teglalap(Pont(100, 50), 10, 5)
    teszt(r.szelesseg == 10 and r.magassag == 5)
    r.forditas()
    teszt(r.szelesseg == 5 and r.magassag == 10)
    # tartalmazza_e
    r = Teglalap(Pont(0, 0), 10, 5)
    teszt(r.tartalmazza_e(Pont(0, 0)))
    teszt(r.tartalmazza_e(Pont(3, 3)))
    teszt(not r.tartalmazza_e(Pont(3, 7)))
    teszt(not r.tartalmazza_e(Pont(3, 5)))
    teszt(r.tartalmazza_e(Pont(3, 4.99999)))
    teszt(not r.tartalmazza_e(Pont(-3, -3)))
    # tegla_kozep
    r1 = Teglalap(Pont(0,0), 1, 1)
    r2 = Teglalap(Pont(0,0), 2, 2)
    teszt(r1.tegla_kozep() == Pont(0.5, 0.5))
    teszt(r2.tegla_kozep() == Pont(1, 1))

    # utkoz_tegla
    r1 = Teglalap(Pont(0,0), 1, 1)
    r2 = Teglalap(Pont(2,2), 1, 1)
    r3 = Teglalap(Pont(0.5,0.5), 1, 1)
    teszt(not r1.utkoz_tegla(r2))
    teszt(r1.utkoz_tegla(r3))
    r1 = Teglalap(Pont(0.5,0.5), 1, 1)
    r2 = Teglalap(Pont(0,0), 2, 2)
    r3 = Teglalap(Pont(2,2), 1, 1)
    teszt(r2.utkoz_tegla(r3))




class Teglalap:
    """[Egy osztály a téglalapok el˝oállításához.]

    Args:
        object ([type]): [description]
    """

    def __init__(self, poz, sz, m):
        """[Inicializálja a téglalapot a poz pozícióra sz szélességgel m magassággal.]

        Args:
            poz ([type]): [description]
            sz ([type]): [description]
            m ([type]): [description]
        """
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m
    
    def __str__(self):
        return "{0}, {1}, {2}".format(self.magassag, self.csucs, self.magassag)

    def noveles(self, delta_szelesseg, delta_magassag):
        """[Növeli (vagy csökkenti) ezt az objektumot a delta értékekkel.]

        Args:
            delta_szelesseg ([type]): [description]
            delta_magassag ([type]): [description]
        """
        self.szelesseg += delta_szelesseg
        self.magassag += delta_magassag
    
    def mozgatas(self, dx, dy):
        """[Elmozdítja ezt az objektumot a delta értékekkel.]

        Args:
            dx ([type]): [description]
            dy ([type]): [description]
        """
        self.csucs.x += dx
        self.csucs.y += dy
    
    def terulet(self):
        """[Adj hozzá egy terulet metódust a Teglalap osztályhoz, amelyet ha meghívunk egy példányra, akkor annak területét adja vissza:]

        Returns:
            [type]: [description]
        """
        return self.szelesseg * self.magassag
    
    def kerulet(self):
        """[Írj egy kerulet metódust a Teglalap osztályon belül, amely segítségével meghatározhatjuk a Teglalap példányok kerületét:]

        Args:
            parameter_list ([type]): [description]
        """
        return (self.magassag + self.szelesseg) * 2

    def forditas(self):
        """[Írj egy forditas metódust a Teglalap osztályon belül, amellyel felcserélhetjük a Teglalap példányok magasságát és szélességét:]
        """
        szelesseg = self.szelesseg
        magassag = self.magassag
        self.magassag = szelesseg
        self.szelesseg = magassag

    def tartalmazza_e(self, p1):
        """[Készíts egy új metódust a Teglalap osztályon belül annak ellen˝orzésére, hogy egy Pont objektum a téglalapon belülre esik-e! Ennél a feladatnál feltételezzük, hogy a téglalap a (0, 0) koordinátán van, a szélessége 10, a magassága pedig 5. A téglalap fels˝o határai nyíltak, tehát a téglalap a [0; 10) tartományt foglalja el az x tengelyen, ahol a 0 a tartomány része, de a 10 nem; y irányban pedig a [0; 5) tartományban áll. Szóval a (10, 2) pontot nem tartalmazza. Ezeken a teszteken át kell, hogy menjen:]

        Args:
            p1 ([type]): [description]
        """
        if p1.x < self.csucs.x:
            return False
        elif p1.x >= self.csucs.x + self.szelesseg:
            return False
        elif p1.y < self.csucs.y:
            return False
        elif p1.y >= self.csucs.y + self.magassag:
            return False
        else:
            return True

    def tegla_kozep(self):
        """[Tegla kozep pontja]
        """
        x = self.csucs.x + (self.szelesseg / 2)
        y = self.csucs.y + (self.magassag / 2)
        return Pont(x, y)
        

    def utkoz_tegla(self, masik_tegla):
        """[Írj egy függvényt, mely meghatározza, hogy két téglalap összeér-e! Segítség: Ez kemény dió! Gondolj át alaposan minden lehet˝oséget, miel˝ott kódolni kezdesz.]

        Args:
            masik_tegla ([type]): [description]
        """
        # Tavolsag a ket kozep pont kozott
        
        r1kozep = self.tegla_kozep()
        r2kozep = masik_tegla.tegla_kozep()
        tavolsag = r1kozep.tavolsag(r2kozep)
        tavolsag = float(abs(tavolsag))

        # Egymas mellet
        if abs(r1kozep.y) == abs(r2kozep.y):
            if tavolsag > self.szelesseg + masik_tegla.szelesseg / 2:
                return False

        # Egymas alatt/felett
        if abs(r1kozep.x) == abs(r2kozep.x):
            if tavolsag > self.magassag + masik_tegla.magassag / 2:
                return False

        # Nincsenek feddesbeb
        a = ((self.szelesseg / 2) + (masik_tegla.szelesseg / 2)) ** 2
        b = ((self.magassag / 2) + (masik_tegla.magassag / 2)) ** 2
        if tavolsag > math.sqrt(a**2 + b**2):
            return False

        return True

tesztkeszlet()