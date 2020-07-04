class Pont:
    """[A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.]
    """

    def __init__(self, x=0, y=0):
        """[Egy új, origóban álló pont létrehozása.]
        """
        self.x = x
        self.y = y

p = Pont(4, 3)
q = Pont(6, 3)
r = Pont()
print(p.x, q.y, r.x)