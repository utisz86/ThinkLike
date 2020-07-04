szerepel_e = "m" in "alma"
print(szerepel_e)
szerepel_e = "i" in "alma"
print(szerepel_e)
szerepel_e = "al" in "alma"
print(szerepel_e)
szerepel_e = "la" in "alma"
print(szerepel_e)

def maganhangzo_torles(s):
    maganhanzok = "aáeéiíoóöőuúüű"
    maganhanzok = maganhanzok + maganhanzok.upper()
    massalhangzos_s = ""
    for k in s:
        if k not in maganhanzok:
            massalhangzos_s += k
    return massalhangzos_s

maganhangzo_torles("informatika") == "nfrmtk"
maganhangzo_torles("aábeéiífoóö˝oujúü˝upAÁEÉIÍOÓÖ˝OUÚÜ˝Us") == "bfjps"


########
def kereses(szoveg, k):
    """
3 Megkeresi a k karaktert a szövegben (szoveg) és visszatér annak
˓→indexével.
4 A visszatérési érték -1, ha a k karakter nem szerepel a szövegben.
5 """
    i = 0
    while i < len(szoveg):
        if szoveg[i] == k:
            return i
        i += 1
    return -1

kereses("Informatika", "o") == 3
kereses("Informatika", "I") == 0
kereses("Informatika", "a") == 6
kereses("Informatika", "x") == -1


#######
def a_betuk_szama(szoveg):
    darab = 0
    for k in szoveg:
        if k == "a":
            darab += 1
    return darab
            

a_betuk_szama("banán") == 1            

#####
def kereses2(szoveg, k, kezdet):
    i = kezdet
    while i < len(szoveg):
        if szoveg[i] == k:
            return i
        i += 1
    return -1

print(kereses2("banan", "n", 2) == 2)


####
ss = "Nos én sose csináltam mondta Alice"
szavak = ss.split()
print(szavak)