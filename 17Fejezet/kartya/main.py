import pygame
import spritesheet
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

    playingCards = spritesheet.spritesheet(os.path.join(image_path, 'playingCards.png'))

    # Sprite is 16x16 pixels at location 0,0 in the file...
    sor = 0
    oszlop = 0
    kartya_kep = playingCards.image_at((sor * 140, oszlop * 190, 139, 189))
    kartya_kepek = []    


    while True:

        # Billenty˝uzet, egér, joystick, stb. események figyelése.
        esemeny = pygame.event.poll()
        if esemeny.type == pygame.QUIT: # Rákattintottak az ablakbezárás gombra?
            break   # Kilépés a ciklusból

        # Minden egyes képkockánál teljesen el˝oröl kezdve rajzoljuk újra a képet:
        # El˝oször mindent háttérszínnel töltünk ki.
        fo_felulet.fill((0, 200, 255))

        # Átmásoljuk a képünket a felület (x, y) pontjára.
        fo_felulet.blit(kartya_kep, (0,0))

        # Most, hogy mindent megrajzoltunk, kirakjuk a képerny˝ore!
        pygame.display.flip()

    pygame.quit()

main()