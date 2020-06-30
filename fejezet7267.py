def gyok(n):
    """[7. Adj egy print függvényt a Newton-féle gyok függvényhez, amely kiíratja a jobb változó értékét minden
cikluslépésben! Hívd meg a módosított függvényt a 25 aktuális paraméterrel, és jegyezd fel az eredményt!]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    kozelites = n/2.0
    itteracio = 0
    while True:
        itteracio += 1
        jobb = (kozelites + n/kozelites)/2.0
        print(jobb)
        if abs(kozelites - jobb) < 0.001:
            print(itteracio)
            return jobb
        kozelites = jobb


# Teszt esetek
print(gyok(25.0))
print(gyok(49.0))
print(gyok(81.0))