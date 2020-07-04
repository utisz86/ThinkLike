import locale
import functools

locale.setlocale(locale.LC_ALL, "HU_hu.UTF8")
szoveg_lista2 = ["én", "te", "ő", "mi", "ti", 'ők']
szoveg_lista2.sort(key=functools.cmp_to_key(locale.strcoll))
print(szoveg_lista2)

def megduplaz(a_list):
    """ Visszaad egy listát, mely az a_list elemeinek kétszeresét tartalmazza. """
    uj_list = []
    for ertek in a_list:
        uj_elem = 2 * ertek
        uj_list.append(uj_elem)

        return uj_list

b_list = [2, 5, 9]
xs = megduplaz(b_list)
print(b_list)
print(xs)


nota = "Esik es˝o, szép csendesen csepereg..."
szavak = nota.split()
print(szavak)

print(nota.split("se"))

ragaszto = ";"
s = ragaszto.join(szavak)
print(s)


xs = list("Mocsári Béka")
print(xs)
print("".join(xs))

def f(n):
    """ Keresse meg az els˝o pozitív egész számot 101 és n között, amely osztható 21-el. """
    for i in range(101,n):
        if (i % 21 == 0):
            return i

print(f(110) == 105)
print(f(1000000000) == 105)