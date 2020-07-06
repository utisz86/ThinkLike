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

    def __mul__(self, masik):
        return self.x * masik.x + self.y * masik.y

    def __rmul__(self, masik):
        return Pont(masik * self.x, masik * self.y)



p1 = Pont(3, 4)
p2 = Pont(5, 7)
    
print(p1 * p2)
print(2 * p2)
print(p2 * 2)    