import os

def mappa_listazas(utvonal):
    """[Visszaadja összes elem rendezett listáját az útvonalon. Ez csak a neveket adja vissza, nem pedig a teljes elérési utat.]

    Args:
        utvonal ([type]): [description]
    """
    mapplista = os.listdir(utvonal)
    mapplista.sort()
    return mapplista

def fajlok_kiiratasa(utvonal, prefix=""):
    """[Az útvonalak tartalmának rekurzív kiíratása.]

    Args:
        utvonal ([type]): [description]
        prefix (str, optional): [description]. Defaults to "".
    """
    if prefix == "":
        print("A mappa kilistazasa ", utvonal)
        prefix = "| "

        mappalista = mappa_listazas(utvonal)
        for f in mappalista:
            print(prefix+f)
            teljesnev = os.path.join(utvonal, f)
            if os.path.isdir(teljesnev):
                fajlok_kiiratasa(teljesnev, prefix + "| ")
        