szuletesi_ev = ("Paris Hilton", 1981)
print(szuletesi_ev)

julia = ("Julia", "Roberts", 1967, "Kettős játék", 2009, "színésznő","Atlanta, Georgia")

print(julia[2]) # 1967

#julia[0] = "X"

(k_nev, v_nev, szul_ev, film, film_ev, foglalkozas, szul_hely) = julia


import math

def f(r):
    """[Visszatér a (kerület, terület) értékekkel egy r sugarú kör esetén]

    Args:
        r ([type]): [description]
    """
    k = 2 * math.pi * r
    t = math.pi * r * r
    return (k, t)

print(f(5))


julia_more_info = ( ("Julia", "Roberts"), (1967, "október", 8), "színészn˝o", ("Atlanta", "Georgia"), [ ("Sztárom a párom", 1999), ("Micsoda n˝o", 1990), ("Ízek, imák, szerelmek", 2010), ("Erin Brockovich", 2000), ("Álljon meg a nászmenet", 1997), ("Egy veszedelmes elme vallomásai", 2002), ("Oceans Twelve", 2004) ])