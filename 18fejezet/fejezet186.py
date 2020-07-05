import pygame, math
pygame.init()   # El˝okészíti a pygame modult a használatra

# Hozz létre egy új felületet és ablakot.
felulet_meret = 1024
fo_felulet = pygame.display.set_mode((felulet_meret,felulet_meret))
my_clock = pygame.time.Clock()

def fa_rajzolasa(rend, szog, sz, pozn, irany, szin=(0, 0, 0), melyseg=0):
    
    torzs_arany = 0.29                  # Milyen nagy a fa törzse az egész fához viszonyítva?
    torzs = sz * torzs_arany            # törzs hossza
    delta_x = torzs * math.cos(irany)
    delta_y = torzs * math.sin(irany)
    (u, v) = pozn
    ujpoz = (u + delta_x, v + delta_y)
    pygame.draw.line(fo_felulet, szin, pozn, ujpoz)

    if rend > 0:                        # Rajzolj egy szintet

        # A következ˝o hat sor egyszer˝u megoldás nyújt arra, hogy a rekurzió a
        # két nagyobb felét eltér˝o szín˝uvé változtassa. Csaljunk itt egy kicsit, hogy
        # megváltoztassuk a színeket a mélységekben, amikor a mélység páros vagy páratlan, stb.
        if melyseg == 0:
            szin1 = (255, 0, 0)
            szin2 = (0, 0, 255)
        else:
            szin1 = szin
            szin2 = szin

        # hívd meg rekurzívan, hogy kirajzolja a két részfát
        ujsz = sz*(1 - torzs_arany)
        fa_rajzolasa(rend-1, szog, ujsz, ujpoz, irany-szog, szin1, melyseg+1)
        fa_rajzolasa(rend-1, szog, ujsz, ujpoz, irany+szog, szin2, melyseg+1)

def gameloop():

    szog = 0
    while True:
        # Kezeld az eseményeket a billenty˝uzettel, egérrel stb.
        esemeny = pygame.event.poll()
        if esemeny.type == pygame.QUIT:
            break;

        # Aktualizálás - változtasd meg a szöget
        szog += 0.01

        # Rajzolj ki mindent
        fo_felulet.fill((255, 255, 0))
        fa_rajzolasa(9, szog, felulet_meret*0.9, (felulet_meret//2, felulet_meret-50), -math.pi/2)

        pygame.display.flip() 
        my_clock.tick(120)

gameloop()
pygame.quit()