import random

# Létrehoz egy fekete doboz objektumot, amely véletlen számokat generál
rng = random.Random()

kocka_dobas = rng.randrange(1, 7) # Vissza ad egy egész éréket, az 1, 2, 3, 4, 5, 6 számok egyikét

kesleltetes_masodpercben = rng.random() * 5.0

kartyak = list(range(52))   # Egész számokat generál [0 .. 51] között,
                            # amely egy kártyacsomagot szimbolizál.
rng.shuffle(kartyak)        # Véletlenszer˝uen összekeveri a kártyákat.

drng = random.Random(123) # Létrehozza az ismert indítási állapotot

