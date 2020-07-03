from fejezet157pont import Pont 
import copy # Ezt a sort a szkript elejére szokás írni.

def azonos_koordinatak(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

# Ezek a sorok az osztály- és függvénydefiníciók alá kerüljenek.
p1 = Pont(3, 4)
p2 = copy.copy(p1)
azonos= p1 is p2
print(azonos)
azonos = azonos_koordinatak(p1, p2)
print(azonos)