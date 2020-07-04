for i in [12, 16, 17, 24, 29, 30]:
    if i % 2:
        continue
    print(i)
print("Kesz")


def tobbszorosok_kiirasa(n, magassag):
    for i in range(1, magassag+1):
        print(n* i, end="  ")
    print()

def szorzotabla_kiiras(magassag):
    for i in range(1, magassag+1):
        tobbszorosok_kiirasa(i, i+1)

szorzotabla_kiiras(7)