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
    # tukrozes_x_tengelyre
    teszt(p.tukrozes_x_tengelyre() == Pont(-5, -3))
    teszt(q.tukrozes_x_tengelyre() == Pont(4, 2))
    # origotol_mert_meredekseg
    teszt(p.origotol_mert_meredekseg() == (3/-5) )
    teszt(q.origotol_mert_meredekseg() == (-2/4) )


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


tesztkeszlet()

