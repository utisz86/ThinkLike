import locale

szo = input("A szavad: ")
locale.setlocale(locale.LC_ALL, "HU_hu.UTF8")

k = locale.strcoll(szo, "banan")

if k < 0:
    print("A szavad, a(z) " + szo + ", a banán elé jön.")
elif k > 0:
    print("A szavad, a(z) " + szo + ", a banán után jön.")
else:
    print("Nem, nincs banánunk!")