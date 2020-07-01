import random

def random_egeszek(szam, also_hatar, felso_hatar):
    """[Véletlenszer˝uen generáljunk egy megadott számú egészeket tartalmazó listát az alsó és fels˝o határ között. A fels˝o határ nyitott.]

    Args:
        szam ([type]): [description]
        also_hatar ([type]): [description]
        felso_hatar ([type]): [description]
    """
    rng = random.Random()
    eredmeny = []
    for i in range(szam):
        eredmeny.append(rng.randrange(also_hatar, felso_hatar))
    return eredmeny

print(random_egeszek(5, 1, 13)) # Válasszunk 5 egész számot véletlenszer˝uen a hónapok sorszámaiból

xs = list(range(1,13)) # Létrehozunk egy listát 1..12-ig (itt nincsenek ismétl˝odések)

rng = random.Random()
rng.shuffle(xs)
eredmeny = xs[:5]
print(eredmeny)

