import turtle

turtle.setup(400, 500)
ablak = turtle.Screen()
ablak.title("Idozito haszanalta")
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color("purple")
Eszti.pensize(3)

def ek1():
    Eszti.forward(100)
    Eszti.left(56)
    ablak.ontimer(ek1, 60)

ek1()
ablak.mainloop()