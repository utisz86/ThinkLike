    """[Nem mondtunk semmit ebben a fejezetben arról, hogy vajon a rendezett n-esek átadhatóak-e függvénynek
paraméterként. Hozz létre egy kis Python példakódot ennek kiderítésére!]
    """

def elso(x):
    return x[0]

x = ("Julia", "Roberts", 1967, "Pénzes cápa", 2016, "színészn˝o", "Atlanta, Georgia")
print(elso(x))

def min_own(x):
    return min(x)

x = (5,3,9,10)
print(min_own(x))

"""[Az értékpár a rendezett n-es általánosítása vagy ez fordítva van?]
"""

"""Az értékpár egyfajta rendezett n-es vagy a rendezett n-es egyfajta értékpár?
9.5."""    