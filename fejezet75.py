for x in range(13):
    print(x, "\t", 2**x)

for i in range(1, 7):
    print(2 * i, end="  ")

print()

def tobbszorosok_kiirasa(n):
    for i  in range(1, 7):
        print(n * i, end="  ")
    print()

tobbszorosok_kiirasa(2)
tobbszorosok_kiirasa(3)

for i in range(1, 7):
    tobbszorosok_kiirasa(i)

def szorzotabla_kiiras():
    for i in range(1, 7):
        tobbszorosok_kiirasa(i)


for i in [12, 16, 17, 24, 29]:
    if i % 2 ==1: # Ha a szam paratlan ...
        break     # ... azonnal hagyd el a ciklust
    print(i)
print("Kesz.")


osszeg = 0
while  True:
    bemenet = input("Add meg a kovetkezo szamot! (hagyd uresen a befejezeshez)")
    if bemenet == "":
        break
    osszeg += int(bemenet)
print("Az altalad megadott szamok osszege: ", osszeg)
        