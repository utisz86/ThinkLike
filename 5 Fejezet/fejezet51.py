def hetnapja(nap):
    napok = ["Hetfo", "Kedd", "Szerda", "Csutortok", "Pentek", "Szombat", "Vasarnap"]

    return(napok[nap])


for i in range(7):
    print(hetnapja(i))
