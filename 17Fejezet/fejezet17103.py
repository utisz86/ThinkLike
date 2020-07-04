    
"""[3. Keress egy kártyalapokat tartalmazó képgy˝ujteményt a kedvenc keres˝omotorod segítségével (ha angol nyelven keresel, akkor több találat várható: „sprite sheet playing cards”). Készíts egy [0, 1, . . . , 51] listát a pakliban lév˝o 52 kártya reprezentálására! Keverd össze a kártyákat és vedd fel az első öt lapot a kezedbe, mint a pókerben az osztásnál! Jelenítsd meg a kezedben lévő lapokat!]
"""

import pygame

def main():
    """[A játék inicializálása és a f˝ociklus futtatása.]
    """
    pygame.init() # El˝okészíti a pygame modult a használatra.
    felulet_meret = 480 # A felület kívánt fizikai mérete pixelben.

    # Egy felület és a hozzá tartozó ablak elkészítése.
    # A set_mode (szélesség, magasság) értékpárt vár.

    fo_felulet = pygame.display.set_mode((felulet_meret, felulet_meret))

    # Egy kis téglalap adatai, beleértve a színét is.
    kis_teglalap = (300, 200, 150, 90)
    valamilyen_szin = (255, 0, 0) # A szín a (piros, zöld, kék) színekb˝ol áll el˝o.

    while True:
        esemeny = pygame.event.poll()   # Események lekérdezése.
        if esemeny.type == pygame.QUIT:  # Az ablakbezárása gombra kattintottak?
            break # ... a játékciklus elhagyása.
        
        # A játék objektumaid, adatszerkezeteid frissítése ide jön.

        # Minden egyes képkockánál teljesen el˝oröl kezdve rajzoljuk újra a képet: 
        # El˝oször mindent háttérszínnel töltünk ki.
        fo_felulet.fill((0, 200, 255))

        

        # A felület most már kész, megkérjük a pygame-et, hogy jelenítse meg!
        pygame.display.flip()
    
    pygame.quit()   # Ha kilépünk a f˝ociklusból, akkor az ablakot is bezárjuk

main()