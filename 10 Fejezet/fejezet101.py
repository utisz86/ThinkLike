import turtle

turtle.setup(400, 500) # Az ablak méretének beállítása
ablak = turtle.Screen() # Az ablak referenciájának lekérése
ablak.title("Billenty˝u leütés kezelése!") # Az ablaknév módosítása
ablak.bgcolor("lightgreen") # Háttér színének beállítása
Eszti = turtle.Turtle() # A kedvenc tekn˝ocünk elkészítése

# A kovetkezo fuggvenyek az esemenykezeloink
def ek1():
    Eszti.forward(30)

def ek2():
    Eszti.left(45)

def ek3():
    Eszti.right(45)

def ek4():
    ablak.bye() # A tekn˝oc ablak bezárása

# Ezek a sorok rendelik össze a billenty˝u leütés eseményeket
# az általunk definiált eseménykezel˝o függvényekkel

ablak.onkey(ek1, "Up")
ablak.onkey(ek2, "Left")
ablak.onkey(ek3, "Right")
ablak.onkey(ek4, "q")

# Most megkérjük az ablakot, hogy kezdje el figyelni az eseményeket.
# Ha bármelyik általunk figyelt billenty˝ut lenyomja valaki, akkor
# a hozzá tartozó eseménykezel˝o meghívásra kerül.
ablak.listen()
ablak.mainloop()