def gyok(n):
    kozelites = n/2.0
    itteracio = 0
    while True:
        itteracio += 1
        jobb = (kozelites + n/kozelites)/2.0
        if abs(kozelites - jobb) < 0.001:
            print(itteracio)
            return jobb
        kozelites = jobb


# Teszt esetek
print(gyok(25.0))
print(gyok(49.0))
print(gyok(81.0))