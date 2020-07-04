import urllib.request

url = "http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf"
cel_fajlnev = "thinkcspy3_en.pdf"

urllib.request.urlretrieve(url, cel_fajlnev)

def weboldal(url):
    """[Visszatér a weboldal tartalmával.
5 A tartalmat sztringgé alakítja, miel˝ott visszatérne.]

    Args:
        url ([type]): [description]
    """
    csatlakozo = urllib.request.urlopen(url)
    adat = str(csatlakozo.readall())
    csatlakozo.close()
    return adat

szoveg = weboldal("http://www.gnu.org/software/make/manual/make.txt")
print(szoveg)