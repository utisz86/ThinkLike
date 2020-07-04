def ablak_keszites(szin, ablaknev):
    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablaknev)
    return a

def teknoc_keszites(szin, tm):
    t = turtle.Turtle()
    t.color(szin)
    t.pensize(tm)


a = ablak_keszites("green", "eszti es sanyi tancol")
Eszti = teknoc_keszites("hotpink", 5)
Sanyi = teknoc_keszites("black", 1)
David = teknoc_keszites("yellow", 2)