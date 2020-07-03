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


#Példa a metódus felhasználása:
p = Pont(3, 4) # Az adott pont objektum
q = Pont(5, 12) # Egy másik pont objektum
r = p.sulypont_szamitas(q) # A súlypont számítása
print(r)

print(Pont(3, 4).sulypont_szamitas(Pont(5, 12)))