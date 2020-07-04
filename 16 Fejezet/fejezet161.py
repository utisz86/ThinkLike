from fejezet157pont import Pont 

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

teglalap = Teglalap(Pont(0,0), 100, 200)
bomba = Teglalap(Pont(100, 80), 5, 10) # A videojátékomban.
print("teglalap: ", teglalap)
print("bomba: ", bomba)

teglalap.magassag += 100
teglalap.szelesseg =+ 50

print("teglalap: ", teglalap)
print("bomba: ", bomba)

r = Teglalap(Pont(10,5), 100, 50)
print(r)

r.noveles(25, -10)
print(r)

r.mozgatas(-10, 10)
print(r)