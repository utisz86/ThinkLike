def sor3np1(n):
    """ Kiírja a 3n+1 sorozatot n-t˝ol amíg el nem éri az 1-et. """

    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end=".\n")

sor3np1(3)
sor3np1(19)
sor3np1(21)
sor3np1(16)