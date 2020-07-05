karakterlanc = input("mi?")

betu_szamlalo = {}

for betu in karakterlanc:
    betu_szamlalo[betu] = betu_szamlalo.get(betu, 0) + 1


betuk = list(betu_szamlalo.items())
betuk.sort()
print(betuk)