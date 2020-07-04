import turtle

turtle.setup(400, 500)
ablak = turtle.Screen()
ablak.title("Ablakon belüli kattintások kezelése")
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color("purple")
Eszti.pensize(3)
Eszti.shape("circle")

def ek1(x, y):
    ablak.title("Kattintás koordinátái: {0}, {1}".format(x, y))
    Eszti.goto(x, y)


ablak.onclick(ek1) # Összerendeljük a kattintás eseményt az eseménykezel˝ovel
ablak.mainloop()
