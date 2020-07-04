def kamatos_kamat(c, r, m, t):
    fv = c * (1 + r/m) ** (m*t)
    return fv

befektetettOsszeg = float(input("Mekkor osszeget kivan befektettni? "))
vegOsszeg = kamatos_kamat(befektetettOsszeg, 0.08, 12, 5)
print("A futamido vegen: ", vegOsszeg)