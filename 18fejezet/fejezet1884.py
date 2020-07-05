import turtle

def sierpinski(t, rend, meret, szinValtoMelyseg=-1):
    """[A 0. rend˝u Sierpinski-háromszög egy egyenl˝o oldalú háromszög. Az 1. rend˝ut le tudjuk rajzolni 3 kisebb háromszögként (itt kissé szétválasztva, azért, hogy segítsen a megértésben.) A 2. és 3. rend˝u háromszög szintén látható. Rajzolj a felhasználó bemenetének megfelel˝o Sieprinski-háromszögeket.]

    Args:
        t ([type]): [description]
        rend ([type]): [description]
        meret ([type]): [description]
    """

    if rend == 0:    # Alapesetben csak egy haromszog
        for i in [0,1,2]:
            t.forward(meret)
            t.left(120)
    else:
        if (szinValtoMelyseg + rend-1) % 2 == 0:
            t.color("red")
        else:
            t.color("blue")
        sierpinski(t, rend-1, meret/2)
        t.forward(meret/2)
        sierpinski(t, rend-1, meret/2)
        t.back(meret/2)
        t.left(60)
        t.forward(meret/2)
        t.right(60)
        sierpinski(t, rend-1, meret/2)
        t.left(60)
        t.back(meret/2)
        t.right(60)
        t.color("purple")
        

# Ablak setup
turtle.setup(1024, 500) # Az ablak méretének beállítása
ablak = turtle.Screen() # Az ablak referenciájának lekérése
ablak.bgcolor("lightgreen")

#Turtle setup
Eszti = turtle.Turtle() # A kedvenc tekn˝ocünk elkészítése
Eszti.penup()
Eszti.goto(-450, 0)
Eszti.pendown()
Eszti.pencolor("blue")
Eszti.speed(20)


for i in [0, 1, 2, 3, 4]:
    Eszti.pendown()
    sierpinski(Eszti, i, 50, szinValtoMelyseg=0)
    Eszti.penup()
    Eszti.forward(100)

# a hozzá tartozó eseménykezel˝o meghívásra kerül.
ablak.mainloop()