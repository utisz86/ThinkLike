import pygame
import os

# Relative paths
current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'images') # The image folder path

def main():
    print(os.getcwd())
    """ A játék inicializálása és a f˝ociklus futtatása. """
    pygame.init() # El˝okészíti a pygame modult a használatra.

    # Egy felület és a hozzá tartozó ablak elkészítése.
    # A set_mode (szélesség, magasság) értékpárt vár.
    fo_felulet = pygame.display.set_mode((960, 480))

    # A PyGame képes kezelni a gif, jpg, png, stb. képformátumokat is.
    cardJoker = pygame.image.load(os.path.join(image_path, 'cardJoker.png'))

    while True:

        # Billenty˝uzet, egér, joystick, stb. események figyelése.
        esemeny = pygame.event.poll()
        if esemeny.type == pygame.QUIT: # Rákattintottak az ablakbezárás gombra?
            break   # Kilépés a ciklusból

        # Minden egyes képkockánál teljesen el˝oröl kezdve rajzoljuk újra a képet:
        # El˝oször mindent háttérszínnel töltünk ki.
        fo_felulet.fill((0, 200, 255))

        # Átmásoljuk a képünket a felület (x, y) pontjára.
        fo_felulet.blit(cardJoker, (100,120))

        # Most, hogy mindent megrajzoltunk, kirakjuk a képerny˝ore!
        pygame.display.flip()

    pygame.quit()

main()