elotag = "Törp"
utotagok_listaja = ["er˝os", "költ˝o", "morgó", "ölt˝o", "papa", "picur","szakáll" ]

for utotag in utotagok_listaja:
    print(elotag + utotag)


s = "A Karib-tenger kalózai"
print(s[0:1]) # A
print(s[2:14]) # Karib-tenger
print(s[15:22]) # kalózai
baratok = ["Misi","Petra","Botond","Jani","Csilla","Peti","Norbi"]
print(baratok[2:4]) # ['Botond', 'Jani']

###
szo = "banan"
if szo == "banan":
    print("Nem, nincs bananunk!")


if szo < "banan":
    print("A szavad, a(z) " + szo + ", a banan ele jon")
elif szo > "banán":
    print("A szavad, a(z) " + szo + ", a banán után jön.")
else:
    print("Nem, nincs banánunk!")