class Pont:
    """[A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.]
    """

    def __init__(self):
        """[Egy új, origóban álló pont létrehozása.]
        """
        self.x = 0
        self.y = 0

p = Pont()  # A Pont osztály egy objektumának létrehozása (példányosítás)
q = Pont()  # Egy második Pont objektum készítése

# Minden Pont objektum saját x és y attribútumokkal rendelkezik
print(p.x, p.y, q.x, q.y)

p.x = 3
p.y = 4
print(p.x, p.y, q.x, q.y)

print("(x={0}, y={1})".format(p.x, p.y))
origotol_mert_tavolsag_negyzete = p.x * p.x + p.y * p.y

print()



