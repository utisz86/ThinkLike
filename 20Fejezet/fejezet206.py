betu_szamlalo = {}
for betu in "Mississippi":
    betu_szamlalo[betu] = betu_szamlalo.get(betu, 0) + 1

print(betu_szamlalo)

betuk = list(betu_szamlalo.items())
betuk.sort()
print(betuk)