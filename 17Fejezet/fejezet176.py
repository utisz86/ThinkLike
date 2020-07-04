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

    def tartalmazza_a_pontot(self, pt):
        """ True-t ad vissza, ha a sprite téglalapja tartalmazza a pt pontot. """
        (sajat_x, sajat_y) = self.pozicio
        sajat_szelesseg = self.kep.get_width()
        sajat_magassag = self.kep.get_height()
        (x, y) = pt
        return ( x >= sajat_x and x < sajat_x + sajat_szelesseg and y >= sajat_y and y < sajat_y + sajat_magassag)

    def kattintas_kezelo(self):
        self.y_sebesseg += -0.3 # Felfele ütjük.

class DukeSprite:
    
    def __init__(self, kep, cel_pozicio):
        """[Létrehoz és inicializál egy királyn˝ot a tábla cél pozíciójában.]

        """
        self.kep = kep
        self.pozicio = cel_pozicio
        self.anim_kepkockak_szama = 0
        self.aktualis_minta_sorszam = 0

    def frissites(self):
        if self.anim_kepkockak_szama > 0:
            self.anim_kepkockak_szama = (self.anim_kepkockak_szama + 1 ) % 60
            self.aktualis_minta_sorszam = self.anim_kepkockak_szama // 6


    def rajzolas(self, cel_felulet):        # Ugyanaz, mint korábban.
        minta_teglalap = (self.aktualis_minta_sorszam * 50, 0,50, self.kep.get_height())
        cel_felulet.blit(self.kep, self.pozicio, minta_teglalap)

    def tartalmazza_a_pontot(self, pt):
        """ True-t ad vissza, ha a sprite téglalapja tartalmazza a pt pontot. """
        (sajat_x, sajat_y) = self.pozicio
        sajat_szelesseg = self.kep.get_width()
        sajat_magassag = self.kep.get_height()
        (x, y) = pt
        return ( x >= sajat_x and x < sajat_x + sajat_szelesseg and y >= sajat_y and y < sajat_y + sajat_magassag)

    def kattintas_kezelo(self):
        if self.anim_kepkockak_szama == 0:
            self.anim_kepkockak_szama = 5

def tabla_rajzolas(kiralynok):
    """ Egy sakktábla rajzolása a kiralynok listával adott királyn˝okkel együtt. """

    pygame.init()

    ora = pygame.time.Clock()

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

    # A sprite lap betöltése.
    duke_sprite_lap = pygame.image.load("duke_spritesheet.png")

    # Két Duke példány létrehozása és elhelyezése a táblán.
    duke1 = DukeSprite(duke_sprite_lap,(mezo_meret*2, 0))
    duke2 = DukeSprite(duke_sprite_lap,(mezo_meret*5, mezo_meret))

    # A példányok hozzáadása a f˝ociklus által kezelt sprite listához.
    osszes_sprite.append(duke1)
    osszes_sprite.append(duke2)

    while True:

        # Billenty˝uzet, egér, stb. események figyelése.
        esemeny=pygame.event.poll()
        if esemeny.type == pygame.QUIT: 
            break

        if esemeny.type == pygame.KEYDOWN:
            key = esemeny.dict["key"]
            if key == 27:   # Escape billenty˝ure ...
                break
            if key == ord("r"):
                szinek[0] = (255, 0, 0) # Váltás piros-feketére.
            elif  key == ord("g"):
                szinek[0] = (0, 255, 0) # Váltás zold-feketére.
            elif key == ord("b"):
                szinek[0] = (0, 0, 255) # Váltás kék-feketére.

        if esemeny.type == pygame.MOUSEBUTTONDOWN: # Egérgomb lenyomva?
            kattintas_helye = esemeny.dict["pos"] # Lekérjük a koordinátákat,
            for spite in osszes_sprite:
                if spite.tartalmazza_a_pontot(kattintas_helye):
                    spite.kattintas_kezelo()
                    break
        
        if esemeny.type != pygame.NOEVENT:  # Csak akkor írjuk ki, ha érdekes!
            print(esemeny)

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
        # Pazarol egy kis id˝ot, hogy a képfrissítés sebessége 60 fps legyen.
        ora.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    tabla_rajzolas([0, 5, 3, 1, 6, 4, 2])   # Az ablak méret tesztelése 7x7- es táblára.
    tabla_rajzolas([6, 4, 2, 0, 5, 7, 1, 3])
    tabla_rajzolas([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1]) # 13 x 13
    tabla_rajzolas([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])



        