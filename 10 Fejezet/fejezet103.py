import turtle

turtle.setup(400, 500)
ablak = turtle.Screen()
ablak.title("Kattintasok kezelese")
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.color("purple")
Sanyi = turtle.Turtle()
Sanyi.color("purple")
Sanyi.forward(100)

def Eszti_esemenykezeloje(x, y):
    ablak.title("Eszti kattintasanak koordinatai: {0}, {1}".format(x, y))
    Eszti.left(42)
    Eszti.forward(30)


def Sanyi_esemenykezeloje(x, y):
    ablak.title("Eszti kattintasanak koordinatai: {0}, {1}".format(x, y))
    Sanyi.left(84)
    Sanyi.forward(50)


Eszti.onclick(Eszti_esemenykezeloje)
Sanyi.onclick(Sanyi_esemenykezeloje)

ablak.mainloop()