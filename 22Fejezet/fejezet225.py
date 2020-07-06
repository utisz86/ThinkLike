class Ido:
    
    def __init__(self, orak=0, percek=0, masodpercek=0):
        """[Egy Ido objektum inicializálása az orak, percek, masodpercek értékekre.]

        Args:
            orak (int, optional): [description]. Defaults to 0.
            percek (int, optional): [description]. Defaults to 0.
            masodpercek (int, optional): [description]. Defaults to 0.
        """
        osszes_masodperc = orak*3600 + percek*60 + masodpercek
        self.orak = osszes_masodperc // 3600
        fennmarado_masodpercek = osszes_masodperc % 3600
        self.percek = fennmarado_masodpercek // 60
        self.masodpercek = fennmarado_masodpercek % 60

    def __str__(self):  # A metódus átnevezése az egyetlen feladatunk
        return "({0}:{1}:{2})".format(self.orak, self.percek, self.masodpercek)

    def novel(self, masodpercek):
        self.masodpercek += masodpercek

        while self.masodpercek >= 60:
            self.masodpercek -= 60
            self.percek += 1

        while self.percek >= 60:
            self.percek -= 60
            self.orak += 1      

    def masodpercre_valtas(self):
        """[A példány által reprezentált másodpercek számával tér vissza]
        """
        return self.orak * 3600 + self.percek * 60 + self.masodpercek 

def ido_osszeadas(i1, i2):
    masodpercek = i1.masodpercre_valtas() + i2.masodpercre_valtas()
    return Ido(0, 0, masodpercek)

aktualis_ido = Ido(9, 14, 30)
aktualis_ido.novel(500)
print(aktualis_ido)