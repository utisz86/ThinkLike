import turtle

def koch(t, rend, meret):
    """[Készíts egy t tekn˝ost és rajzolj egy megadott 'rend˝u' és 'méret˝u' Koch fraktált. Hagyjuk a tekn˝ost ugyanabban az irányban.]

    Args:
        t ([type]): [description]
        rend ([type]): [description]
        meret ([type]): [description]
    """
    
    if rend == 0:           # Alapesetben csak egy egyenes
        t.forward(meret)
    else:
        for szog in [60, -120, 60, 0]:
            koch(t, rend-1, meret/3)
            t.left(szog)

# Ablak setup
turtle.setup(400, 500) # Az ablak méretének beállítása
ablak = turtle.Screen() # Az ablak referenciájának lekérése
ablak.bgcolor("lightgreen")

#Turtle setup
Eszti = turtle.Turtle() # A kedvenc tekn˝ocünk elkészítése
Eszti.pencolor("blue")

for i in range(6):
    koch(Eszti, 1, 60)
    Eszti.left(60)
    koch(Eszti, 1, 60)
    Eszti.right(120)
    
# a hozzá tartozó eseménykezel˝o meghívásra kerül.
ablak.mainloop()