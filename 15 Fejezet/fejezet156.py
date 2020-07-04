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


# tesztek
p = Pont(3, 4)
print(p.x)
print(p.y)
print(p.origotol_mert_tavolsag())

q = Pont(5, 12)
print(q.x)
print(q.y)
print(q.origotol_mert_tavolsag())

r = Pont()
print(r.x)
print(r.y)
print(r.origotol_mert_tavolsag())


def pont_kiiras(pt):
    print("({0}, {1})".format(pt.x, pt.y))

pont_kiiras(r)