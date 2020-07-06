class Ido:

    def __init__(self, orak=0, percek=0, masodpercek=0):
        """[Egy Ido objektum inicializálása az orak, percek, masodpercek értékekre.]

        Args:
            orak (int, optional): [description]. Defaults to 0.
            percek (int, optional): [description]. Defaults to 0.
            masodpercek (int, optional): [description]. Defaults to 0.
        """
        self.orak = orak
        self.percek = percek
        self.masodpercek = masodpercek

    def __str__(self):  # A metódus átnevezése az egyetlen feladatunk
        return "({0}:{1}:{2})".format(self.orak, self.percek, self.masodpercek)

def ido_osszeadas(i1, i2):
    orak = i1.orak + i2.orak
    percek = i1.percek + i2.percek
    masodpercek = i1.masodpercek + i2.masodpercek
    ossz_ido = Ido(orak, percek, masodpercek)
    return ossz_ido

def ido_osszeadas(i1, i2):

    orak = i1.orak + i2.orak
    percek = i1.percek + i2.percek
    masodpercek = i1.masodpercek + i2.masodpercek

    if masodpercek >= 60:
        masodpercek -= 60
        percek += 1
    
    if percek >= 60:
        percek -= 60
        orak += 1

    ossz_ido = Ido(orak, percek, masodpercek)
    return ossz_ido


aktualis_ido = Ido(9, 14, 30)
kenyersutes_idotartama = Ido(3, 35, 0)
befejezes_ideje = ido_osszeadas(aktualis_ido, kenyersutes_idotartama)
print(befejezes_ideje)


def novel(ido, masodpercek):
    ido.masodpercek += masodpercek

    while ido.masodpercek >= 60:
        ido.masodpercek -= 60
        ido.percek += 1

    while ido.percek >= 60:
        ido.percek -= 60
        ido.orak += 1