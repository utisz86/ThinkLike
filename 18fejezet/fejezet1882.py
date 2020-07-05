import turtle

def Cesaro(t, rend, meret, tores=10):
    """[Rajzolj egy Cesaro-fraktált, a felhasználó által megadott rendben. Megmutatjuk a vonalak négy különböz˝o rendjét a 0, 1, 2, 3-at. Ebben a példában a törés szöge 10 fokos.]

    Args:
        t ([type]): [description]
        rend ([type]): [description]
        meret ([type]): [description]
    """
    if rend == 0: # Alapesetben csak egy egyenes
        t.forward(meret)
    else:
        for szog in [270+tores, 180-2*tores, 270+tores, 0]:
            Cesaro(t, rend-1, meret/3)
            t.left(szog)

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


for i in [0, 1, 2, 3]:
    Eszti.pendown()
    Cesaro(Eszti, i, 150, tores=0)
    Eszti.penup()
    Eszti.forward(100)

# a hozzá tartozó eseménykezel˝o meghívásra kerül.
ablak.mainloop()