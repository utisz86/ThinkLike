lovasok = ["háború", "éhínség", "pestis", "halál"]

for i in [0, 1, 2, 3]:
    print(lovasok[i])

for i in range(len(lovasok)):
    print(lovasok[i])


print("pestis" in lovasok)
print("dezertálás" in lovasok)
print("dezertálás" not in lovasok)





hallgatok = [("Jani", ["Informatika", "Fizika"]), ("Kata", ["Matematika", "Informatika", "Statisztika"]), ("Peti", ["Informatika", "Könyvelés", "Közgazdaságtan", "Menedzsment"]), ("Andi", ["Információs Rendszerek", "Könyvelés", "Közgazdaságtan", "Vállalkozási Jog"]), ("Linda", ["Szociológia", "Közgazdaságtan", "Jogi ismeretek", "Statisztika", "Zene"])]

szamlalo = 0
for (nev, targyak) in hallgatok:
    if "Informatika" in targyak:
        szamlalo =+ 1
print("Az Informatikát felvett hallgatók száma:", szamlalo)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

d = [0] * 4
print(d)
e = [1, 2, 3] * 3
print(e)

a_list = ["a", "b", "c", "d", "e", "f"]
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])


gyumolcs = ["banán", "alma", "eper"]
gyumolcs[0] = "körte"
gyumolcs[2] = "narancs"
print(gyumolcs)

sajat_sztring = "ADAT"
#sajat_sztring[3] = "G"

a = ["egy", "kett˝o", "három"]
del a[1]
print(a)


a = [1, 2, 3]
b = a[:]
print(b)

for szam in range(20):
    if szam % 3 == 0:
        print(szam)

for filmek in ["vígjáték", "animációs", "romantikus"]:
    print("Én szeretem a " + filmek + "et!")


xs = [1, 2, 3, 4, 5]
for i in range(len(xs)):
    xs[i] = xs[i]**2

print(xs, end="\n")
for (i, v) in enumerate(["banán", "alma", "körte", "citrom"]):
    print(i, v)

def megduplaz(a_list):
    """ Átírjuk a lista minden elemét a kétszeresére. """
    for (idx, ert) in enumerate(a_list):
        a_list[idx] = 2 * ert

b_list = [2, 5, 9]
megduplaz(b_list)
print(b_list)