ellentetek = {"fel": "le", "jó": "rossz", "igen": "nem"}
alnev = ellentetek
masolat = ellentetek.copy()

alnev["jo"] = "hibas"
print(ellentetek["jó"])


masolat["jó"] = "téves"
print(ellentetek["jó"])