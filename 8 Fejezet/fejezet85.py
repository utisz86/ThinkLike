s1 = "A nevem {0}!".format("Artur")
print(s1)

nev = "Alice"
kor = 10
s2  = "A nevem {1}, es {0} eves vagyok".format(kor, nev)
print(s2)

n1 = 4
n2 = 5
s3 = "2**10 = {0} es {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
print(s3)

n1 = "Paris"
n2 = "Whitney"
n3 = "Hilton"

print("A pi értéke három tizedesjegyig: {0:.3f}".format(3.1415926))
print("123456789 123456789 123456789 123456789 123456789 123456789")
print("|||{0:<12}|||{1:^12}|||{2:>12}|||Születési év: {3}|||".format(n1, n2, n3, 1981))
print("A {0} decimális érték {0:x} hexadecimális értékké konvertálódik.".format(123456))


elrendezes = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"
print(elrendezes.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(elrendezes.format(i, i ** 2, i ** 3, i ** 5, i ** 10, i ** 20))