def read_reverse(beolvas, kiir):
    """[Írj egy olyan programot, amely beolvas egy fájlt, és a sorait fordított sorrendben írja be egy új fájlba (például az
els˝o sor a régi fájlban az utolsó, és az utolsó sor a régi fájlban az els˝o).]

    Args:
        beolvas ([type]): [description]
        kiir ([type]): [description]
    """
    g = open(kiir, "w")
    for line in reversed(list(open(beolvas))):
        g.write(line)
    g.close()

read_reverse("text.txt", "kiir.txt")