# A keres˝o (Crawler) feltérképezi a fájlrendszert, és létrehoz egy szótárt
import os

def fajl_kereso(ut):
    """[Rekurzívan járd be az összes fájlt a megadott útvonalon]

    Args:
        ut ([type]): [description]
    """
    # Add meg az aktuális mappában lév˝o összes bejegyzést.
    mappa_lista = os.listdir(ut)
    for f in mappa_lista:
        # Alakítsd az egyes neveket elérési úttá.
        teljes_nev = os.path.join(ut, f)

        # Ha ez egy könyvtár, folytasd.
        if os.path.isdir(teljes_nev):
            fajl_kereso(teljes_nev)
        else:   # Csinálj valami hasznosat a fájllal.
            print("{0:30 {1}".format(f, teljes_nev) )


fajl_kereso("C:\\Python32")            