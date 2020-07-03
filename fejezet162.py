from fejezet157pont import Pont 

p1 = Pont(3, 4)
p2 = Pont(3, 4)
print(p1 is p2)
p3 = p1
print(p1 is p3)

def azonos_koordinatak(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

p1 = Pont(3, 4)
p2 = Pont(3, 4)
egy_pont = azonos_koordinatak(p1, p2)
print(egy_pont)


p = Pont(4, 2)
s = Pont(4, 2)
print("Az == eredménye Pontokra alkalmazva:", p == s)
# Alapértelmezés szerint az == a Pont objektumoknál
# referencia szerinti egyenl˝oséget néz.

a = [2,3]
b = [2,3]
print("Az == eredménye listákra alkalmazva:", a == b)
# A listáknál viszont az érték szerinti egyenl˝oségvizsgálat
# az alapértelmezett.