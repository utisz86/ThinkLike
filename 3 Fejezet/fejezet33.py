import turtle

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.shape("turtle")
Eszti.color("blue")

Eszti.penup()
meret = 20

for i in range(30):
    Eszti.stamp()
    meret = meret + 3
    Eszti.forward(meret)
    Eszti.right(24)

ablak.mainloop()
