import turtle

def tobbszinu_negyzet_rajzolas(t, h):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(h)
        t.left(90)

a = turtle.Screen()
a.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.pensize(3)

meret = 20

for i in range(15):
    tobbszinu_negyzet_rajzolas(Eszti, meret)
    meret = meret + 10
    Eszti.forward(10)
    Eszti.right(18)


a.mainloop()
