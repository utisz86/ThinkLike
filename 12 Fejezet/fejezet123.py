import random

def random_egeszek_duplikatum_nelkul(szam, also_hatar, felso_hatar):
    """[Véletlenszer˝uen generáljunk egy megadott számú egészeket tartalmazó
˓→listát
5 az alsó és fels˝o határ között. A fels˝o határ nyitott. Az eredménylista
˓→nem
6 tartalmazhat duplikátumokat.]

    Args:
        szam ([type]): [description]
        also_hatar ([type]): [description]
        felso_hatar ([type]): [description]
    """
    eredmeny = []
    rng = random.Random()
    for i in range(szam):
        while True:
            valasztott = rng.randrange(also_hatar, felso_hatar)
            if valasztott not in eredmeny:
                break
        eredmeny.append(valasztott)
    return eredmeny

xs = random_egeszek_duplikatum_nelkul(5, 1, 10000000)
print(xs)
xs = random_egeszek_duplikatum_nelkul(10, 1, 6)
print(xs)