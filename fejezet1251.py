import modul1
import modul2

print(modul1.kerdes)
print(modul1.valasz)

print(modul2.kerdes)
print(modul2.valasz)

def f():
    n = 7
    print("n kiirasa az f-ben:", n)

def g():
    n = 42
    print("n kiirasa a g-ben", n)

n = 11
print("n kiírása az f hívása el˝ott:", n)
f()
print("n kiírása az f hívása után:", n)
g()
print("n kiírása a g hívása után:", n)