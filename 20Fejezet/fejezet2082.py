d = {"alma": 15, "banán": 35, "szo˝lo˝": 12}
print(d["banán"])

d["narancs"] = 20
print(len(d))

print("szo˝lo˝" in d)

print(d["körte"])

print(d.get("körte", 0))

gyumolcs = list(d.keys())
gyumolcs.sort()
print(gyumolcs)

del d["alma"]
print("alma" in d)