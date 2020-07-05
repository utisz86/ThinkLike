hun2esp = {"egy": "uno", "kett˝o": "dos", "három": "tres"}

for k in hun2esp.keys():
    print("A(z) ", k, " kulcs a lekepezi a(z)", hun2esp[k], " erteket.")

ks = list(hun2esp.keys())
print(ks)

for k in hun2esp:
    print("A kulcs", k)

print(list(hun2esp.values()))


print(list(hun2esp.items()))

for (k,v) in hun2esp.items():
    print("A(z)", k, "leképezése a(z) ", v, ".")


print("egy" in hun2esp)    