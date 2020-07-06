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

    def kesobb_van_e(self, ido2):
        """[Igazzal tér vissza, ha szigorúan nagyobb vagyok, mint az ido2.]

        Args:
            ido2 ([type]): [description]
        """

        if self.orak > ido2.orak:
            return True
        if self.orak < ido2.orak:
            return False

        if self.percek > ido2.percek:
            return True
        if self.percek < ido2.percek:
            return False
        if self.masodpercek > ido2.masodpercek:
            return True

        return False


aktualis_ido = Ido(9, 14, 30)
befejezes_ideje = Ido(9,13,00)

if aktualis_ido.kesobb_van_e(befejezes_ideje):
    print("A kenyer kesz lesz, mielott elkezdenenk sutni!")

