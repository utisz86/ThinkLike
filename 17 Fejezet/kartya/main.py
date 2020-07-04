import pygame

def main():
    """ A játék inicializálása és a f˝ociklus futtatása. """
    pygame.init() # El˝okészíti a pygame modult a használatra.

    # Egy felület és a hozzá tartozó ablak elkészítése.
    # A set_mode (szélesség, magasság) értékpárt vár.
    fo_felulet = pygame.display.set_mode((480, 240))

    while True:

        # Billenty˝uzet, egér, joystick, stb. események figyelése.
        esemeny = pygame.event.poll()
        if esemeny.type == pygame.QUIT: # Rákattintottak az ablakbezárás gombra?
            break   # Kilépés a ciklusból

        # Minden egyes képkockánál teljesen el˝oröl kezdve rajzoljuk újra a képet:
        # El˝oször mindent háttérszínnel töltünk ki.
        fo_felulet.fill((0, 200, 255))

        # Most, hogy mindent megrajzoltunk, kirakjuk a képerny˝ore!
        pygame.display.flip()

    pygame.quit()

main()