import pygame

gravitacio = 0.0001

class KiralynoSpite:

    def __init__(self, kep, cel_pozicio):
        """[Létrehoz és inicializál egy királyn˝ot a tábla cél pozíciójában.]

        """
        self.kep = kep
        self.cel_pozicio = cel_pozicio
        (x, y) = cel_pozicio
        self.pozicio = (x, 0)       # Az oszlop tetejét˝ol indul a labda,
        self.y_sebesseg = 0         # 0 kezd˝osebességgel.

    def frissites(self):
        self.y_sebesseg += gravitacio   # A gravitáció módosítja a sebességet.
        (x, y) = self.pozicio
        uj_y_poz = y + self.y_sebesseg  # A sebesség új pozícióba
        (cel_x, cel_y) = self.cel_pozicio   # A cél pozíció kicsomagolása.
        tav = cel_y - uj_y_poz              # Milyen messze van a padló?

        if tav < 0:                     # A padló alatt vagyunk?
            self.y_sebesseg = -0.75 * self.y_sebesseg
            uj_y_poz = cel_y + tav      # visszapattanás

        self.pozicio = (x, uj_y_poz)       # Visszatérés a padló fölé.

    def rajzolas(self, cel_felulet):        # Ugyanaz, mint korábban.
        cel_felulet.blit(self.kep, self.pozicio)    




def tabla_rajzolas(kiralynok):
    """ Egy sakktábla rajzolása a kiralynok listával adott királyn˝okkel együtt. """

    pygame.init()
    szinek = [(255,0,0), (0,0,0)]   # A színek beállítása [piros, fekete].

    n = len(kiralynok)              # A tábla mérete: nxn.
    felulet_meret = 480             # A felület javasolt fizikai mérete.
    mezo_meret = felulet_meret // n # A négyzetek oldalhosszúsága.
    felulet_meret = n * mezo_meret  # Az n négyzet méretéhez igazítjuk a felületet.

    # Elkészítjük a felületet (szélesség, magasság) és a hozzá tartozó ablakot.
    felulet = pygame.display.set_mode((felulet_meret, felulet_meret))

    labda = pygame.image.load("labda.png")
    labda = pygame.transform.scale(labda, (mezo_meret, mezo_meret))

    # A labda négyzeten belüli középre igazításhoz szükséges eltolás.
    # Ha a négyzet túl kicsi, az eltolás negatív lesz,
    # de akkor is középre kerül a labda :-).
    labda_eltolas = (mezo_meret - labda.get_width()) // 2

    osszes_sprite = [] # Lista a játék összes sprite-ja részére.

    # Egy-egy sprite készítése minden királyn˝ohöz,
    # és a spirte hozzáadása a listához.
    for (oszlop, sor) in enumerate(kiralynok):
        kiralyno = KiralynoSpite(labda, (oszlop*mezo_meret+labda_eltolas, sor*mezo_meret+labda_eltolas))
        osszes_sprite.append(kiralyno)

    while True:

        # Billenty˝uzet, egér, stb. események figyelése.
        esemeny=pygame.event.poll()
        if esemeny.type == pygame.QUIT:
            break;

        # Minden sprite-ot megkérünk, hogy frissítse magát.
        for spite in osszes_sprite:
            spite.frissites()

        # Új háttér rajzolása (egy üres sakktábla).
        for sor in range(n):                # Az összes sor megrajzolása.
            szin_index = sor % 2            # A kezd˝oszín megváltoztatása minden sorban.
            for oszlop in range(n):         # Az oszlopokat bejárva kirajzoljuk a mez˝oket.
                mezo = (oszlop*mezo_meret, sor*mezo_meret, mezo_meret, mezo_meret)
                felulet.fill(szinek[szin_index], mezo)
                # A következ˝o mez˝o rajzolása el˝ott megváltoztatjuk a szín indexét.
                szin_index = (szin_index + 1) % 2

        # Minden sprite-ot megkérünk, hogy rajzolja ki magát.
        for spite in osszes_sprite:
            spite.rajzolas(felulet)


        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    tabla_rajzolas([0, 5, 3, 1, 6, 4, 2])   # Az ablak méret tesztelése 7x7- es táblára.
    tabla_rajzolas([6, 4, 2, 0, 5, 7, 1, 3])
    tabla_rajzolas([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1]) # 13 x 13
    tabla_rajzolas([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])



        