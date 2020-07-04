import pygame
import time
import random



class Kartya(object):
    def __init__(self, kep, cel_pozicio):
        self.kep = kep
        (x, y) = cel_pozicio
        self.pozicio = (x, 0)

    def rajzolas(self, cel_felulet):
        cel_felulet.blit(self.kep, self.pozicio)


    
        

def main(kartyak):
    pygame.init() # El˝okészíti a pygame modult a használatra.
    fo_felulet = pygame.display.set_mode((960, 480))

    
    # Betölti a rajzolandó képet. Cseréld ki a sajátodra.
    # A PyGame képes kezelni a gif, jpg, png, stb. képformátumokat is.
    kartyak=pygame.image.load("playingCards.png")

    kepkockak_szama = 0
    fps = 0
    t0 = time.process_time()

    while True:

        # Billenty˝uzet, egér, joystick, stb. események figyelése.
        esemeny = pygame.event.poll()
        if esemeny.type == pygame.QUIT: # Rákattintottak az ablakbezárás gombra?
            break   # Kilépés a ciklusból

        # A játéklogika egy másik darabja
        kepkockak_szama += 1
        if kepkockak_szama % 500 == 0:
            t1 = time.process_time()
            fps = 500 / (t1 - t0)
            t0 = t1

        # Teljesen újrarajzoljuk a felületet, a háttérszínnel kezdjük.
        fo_felulet.fill((0, 200, 255))

        # Lista a kartyakrol
        osszes_sprite = []

        # Egy-egy sprite keszitese minden kartyahoz, es a sprite hozzadas a listahoz

        for (oszlop, sor) in 



        # Megjeleniti a kartyakat
        for (i, kartya_szam) in xs[:5]:
            fo_felulet.blit(kartyak, (100,120))

        # Most, hogy mindent megrajzoltunk, kirakjuk a képerny˝ore!
        pygame.display.flip()

    pygame.quit()


# Megkeveri a paklit
xs = list(range(52))
rng = random.Random()
rng.shuffle(xs)
print(xs[:5])
main(xs[:5])