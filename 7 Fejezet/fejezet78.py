szultesi_ev = ("Paris Hilton", 1981)

celebek = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), ("Justin Bieber", 1994)]

print(celebek)
print(len(celebek))

for (nev, ev) in celebek:
    if ev < 1980:
        print(nev)


hallgatok = [
    ("Jani", ["Informatika", "Fizika"]),
    ("Kata", ["Matematika", "Informatika", "Statisztika"]),
    ("Peti", ["Informatika", "Könyvelés", "Közgazdaságtan", "Menedzsment"]),
    ("Andi", ["Információs rendszerek", "Könyvelés", "Közgazdaságtan", "Vállalkozási jog"]),
    ("Linda", ["Szociológia", "Közgazdaságtan", "Jogi ismeretek","Statisztika", "Zene"])]

for (nev, targyak) in hallgatok:
    print(nev, "felvett", len(targyak), "kurzust.")

szamlalo = 0
for (nev, targyak) in hallgatok:
    if "Informatika" in targyak:
        szamlalo += 1
print("Az Informatikát felvett hallgatók száma:", szamlalo)