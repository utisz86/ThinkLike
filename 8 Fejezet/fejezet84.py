import sys
import string

def teszt(sikeres_teszt):
    """ Egy test eredmenyenek megjelenitese.    """
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z) {0}. sorban allo teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban allo teszt SIKERTELEN".format(sorszam))

    print(msg)

def tesztkeszlet():
    """ Az ehhez a modulhoz (fajlhoz) tartozo tesztkeszlet futtatasa. """
    teszt(abs(-5) == 5)
    #
    teszt(irasjel_eltavolitas('"Nos, én sose csináltam!" - mondta Alice') =="Nos én sose csináltam mondta Alice")
    teszt(irasjel_eltavolitas("Teljesen, de teljesen biztos vagy benne?") =="Teljesen de teljesen biztos vagy benne")





def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli
            

tesztkeszlet()            

a_tortenetem = """A pitonok nem méreggel ölnek, hanem kiszorítják a szuszt az áldozatukból.  A prédájuk köré tekerik magukat, minden egyes lélegzeténél egy kicsit szorosabban, egészen addig, amíg a légzése abba nem marad. Amint megáll a zsákmány szíve, lenyelik az egészet. A bunda és a tollazat kivételével az egész állat a kígyó gyomrába lesz temetve. Mit gondolsz, mi történik a lenyelt bundával, tollakkal, cs˝orökkel és tojáshéjakkal? A felesleges 'dolgok' távoznak, -- jól gondolod -- kígyó ÜRÜLÉK lesz bel˝olük!"""



szavak = irasjel_eltavolitas(a_tortenetem).split()

print(szavak)