def masol_sr(beolvas, kiir):
    """[Írj egy olyan programot, amely beolvas egy szöveges fájlt, és egy kimeneti fájlt hoz létre, amely az eredeti
fájl másolata, kivéve, hogy minden egyes sor els˝o öt oszlopa tartalmaz egy négyjegy˝u sorszámot, amelyet egy
szóköz követ. A kimeneti fájl sorszámozását 1-t˝ol kezd. Gy˝oz˝odj meg arról, hogy minden egyes sorszám
ugyanolyan széles a kimeneti fájlban. Használd az egyik Python programot, teszt adatként ehhez a feladathoz:
a kimenet a Python program kiírt és sorszámozott listája kell legyen.]

    Args:
        beolvas ([type]): [description]
        kiir ([type]): [description]
    """
    g = open(kiir, "w")
    for (i,line) in enumerate(list(open(beolvas))):
        g.write("{0}\t".format(i+1)+line)
    g.close()

masol_sr("text2.txt", "kiir2.txt")