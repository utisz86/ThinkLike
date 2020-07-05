hun2esp = {}
hun2esp["egy"] = "uno"
hun2esp["ketto"] = "dos"

print(hun2esp)

hun2esp = {"egy": "uno", "kett˝o": "dos", "három": "tres"}

print(hun2esp["kett˝o"])

# A del utasítás eltávolít egy kulcs:érték párt a szótárból.
keszlet = {"alma": 430, "banán": 312, "narancs": 525, "körte": 217}
print(keszlet)

del keszlet["körte"]
print(keszlet)

keszlet["körte"] = 0
print(keszlet)

keszlet["banán"] += 200
print(keszlet)

print(len(keszlet))