import pygame
import time

def main():
    pygame.init() # El˝okészíti a pygame modult a használatra.
    fo_felulet = pygame.display.set_mode((480, 240))

    # Betölti a rajzolandó képet. Cseréld ki a sajátodra.
    # A PyGame képes kezelni a gif, jpg, png, stb. képformátumokat is.
    labda=pygame.image.load("labda.png")

    # Egy font objektum készítése a szöveg rendereléséhez.
    betukeszlet=pygame.font.SysFont("Courier", 16)

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

        # Elhelyezünk egy piros téglalapot valahol a felületen.
        fo_felulet.fill((255, 0, 0), (300, 100, 150, 90))

        # Átmásoljuk a képünket a felület (x, y) pontjára.
        fo_felulet.blit(labda, (100,120))

        # Egy új felületet készítünk, mely a szöveg képét tartalmazza.
        szoveg = betukeszlet.render("Képkocka: {0}, sebesség: {1:.2f} fps".format(kepkockak_szama, fps), True, (0, 0, 0))

        # Átmásoljuk a szöveg felületét a f˝ofelületre.  
        fo_felulet.blit(szoveg, (10, 10))

        # Most, hogy mindent megrajzoltunk, kirakjuk a képerny˝ore!
        pygame.display.flip()

    pygame.quit()

main()