sajat_fajl = open("elso.txt", "w")
sajat_fajl.write("Az elso python faj\n")
sajat_fajl.write("--------------\n")
sajat_fajl.write("Hello, vilag\n")
sajat_fajl.close()


uj_kezelo = open("elso.txt", "r")   # Nyisd meg a fájlt
while True:
    sor = uj_kezelo.readline()      # Próbáld beolvasni a következ˝o sort
    if len(sor) == 0:               # Ha nincs több sor
        break                       # Hagyd el a ciklust
    # Most dolgozd fel az éppen aktuálisan beolvasott sort
    print(sor, end="")

uj_kezelo.close()                   # Zárd be a fájlt

uj_kezelo = open("nincs_ilyen.txt", "r")