def masol_desr(beolvas, kiir):
    """[Írj egy olyan programot, amely megszünteti az el˝oz˝o gyakorlat számozását: ennek egy beszámozott sorokat
tartalmazó fájlt kellene beolvasnia, és egy másik fájlt el˝oállítani a sorszámok nélkül.]

    Args:
        args ([type]): [description]
    """
    g = open(kiir, "w")
    for (i,line) in enumerate(list(open(beolvas))):
        g.write(line.replace("{0}\t".format(i+1),""))
    g.close()

masol_desr("kiir2.txt", "kiir3.txt")