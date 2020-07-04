import random
vel = random.Random()

szam = vel.randrange(1, 1000)

tippszam = 0
uzenet = ""

while True:
    tipp = int(input(uzenet + "\nTaláld ki az 1 és 1000 közötti számot, amire gondoltam:"))
    tippszam += 1
    if tipp > szam:
        uzenet += str(tipp) + " túl nagy.\n"
    elif tipp < szam:
        uzenet += str(tipp) + " túl kicsi.\n"
    else:
        break

input("\n\nNagyszer˝u, kitaláltad {0} tipp segítségével!\n\n".format(tippszam))