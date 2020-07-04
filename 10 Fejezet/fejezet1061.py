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

def ekR():
    Eszti.color("red")

def ekG():
    Eszti.color("green")

def ekB():
    Eszti.color("blue")

def ekmeret_plus():
    pensize = min(Eszti.pensize()+1,20)
    Eszti.pensize(pensize)
    
def ekmeret_minus():
    pensize = max(Eszti.pensize()-1,0)
    Eszti.pensize(pensize)

def pen_up():
    Eszti.penup()

def pen_down():
    Eszti.pendown()

# Ezek a sorok rendelik össze a billenty˝u leütés eseményeket
# az általunk definiált eseménykezel˝o függvényekkel

ablak.onkey(ek1, "Up")
ablak.onkey(ek2, "Left")
ablak.onkey(ek3, "Right")
ablak.onkey(ek4, "q")

ablak.onkey(ekR, "r")
ablak.onkey(ekG, "g")
ablak.onkey(ekB, "b")

ablak.onkey(ekmeret_plus, "=")
ablak.onkey(ekmeret_minus, "-")

ablak.onkey(pen_up, "u")
ablak.onkey(pen_down, "d")

# Most megkérjük az ablakot, hogy kezdje el figyelni az eseményeket.
# Ha bármelyik általunk figyelt billenty˝ut lenyomja valaki, akkor
# a hozzá tartozó eseménykezel˝o meghívásra kerül.
ablak.listen()
ablak.mainloop()