import turtle

def negyzet_rajzolas(t, h):
    for i in range(4):
        t.forward(h)
        t.left(90)

a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("Sanyi talalkozik egy fuggvennyel")

Sanyi = turtle.Turtle()
negyzet_rajzolas(Sanyi, 50)

a.mainloop()
