import turtle

bgcolor = input("Milyen hatterszin: ")

ablak = turtle.Screen()
ablak.bgcolor(bgcolor)
ablak.title("Hello, Eszti!")

pencolor = input("Milyen tol szin: ")

Eszti = turtle.Turtle()
Eszti.color(pencolor)
Eszti.pensize(3)

Eszti.forward(50)
Eszti.left(120)
Eszti.forward(50)

ablak.mainloop()
