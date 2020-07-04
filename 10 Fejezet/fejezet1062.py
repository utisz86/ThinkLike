import turtle

turtle.setup(400, 500)
ablak = turtle.Screen()
ablak.title("Eszti kozlekedesi  lampava valik")
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()


def doboz_rajzolas():
    """ Egy csinos doboz rajzolása a közlekedési lámpa számára """
    Eszti.pensize(3)
    Eszti.color("black", "darkgrey")
    Eszti.begin_fill()
    Eszti.forward(80)
    Eszti.left(90)
    Eszti.forward(200)
    Eszti.circle(40, 180)
    Eszti.forward(200)
    Eszti.left(90)
    Eszti.end_fill()


doboz_rajzolas()

Eszti.penup()
# Eszti pozícionálása oda, ahol a zöld lámpának kell lennie
Eszti.forward(40)
Eszti.left(90)
Eszti.forward(50)
# Esztit egy nagy zöld körré alakítjuk át
Eszti.shape("circle")
Eszti.shapesize(3)
Eszti.fillcolor("green")

# A közlekedési lámpa egyfajta állapotautomata, három állapottal:
# zölddel, sárgával és pirossal. Az állapotokat rendre
# 0, 1, 2 számokkal írjuk le.
# Az állapotváltásnál Eszti helyzetét és színét változtatjuk meg.

# Ez a változó hordozza az aktuális állapotot
allapot_sorszam = 0


def allapot_automata_esemenykezeloje():
    global allapot_sorszam
    if allapot_sorszam == 0:
        Eszti.forward(70)
        Eszti.fillcolor("orange")
        allapot_sorszam = 1
    elif allapot_sorszam == 1:
        Eszti.forward(70)
        Eszti.fillcolor("red")
        allapot_sorszam = 2
    else:
        Eszti.back(140)
        Eszti.fillcolor("green")
        allapot_sorszam = 0
    ablak.ontimer(allapot_automata_esemenykezeloje, 60)


allapot_automata_esemenykezeloje()
ablak.mainloop()