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

def sulypont_szamitas(p1, p2):
    """[Visszatér a p1 és p2 pontok súlypontjával.]

    Args:
        p1 ([type]): [description]
        p2 ([type]): [description]
    """
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return Pont(mx, my)

# teszt
p = Pont(3, 4)
q = Pont(5, 12)
r = sulypont_szamitas(p, q)
print(r)
