def koch(t, rend, meret):
    """[Készíts egy t tekn˝ost és rajzolj egy megadott 'rend˝u' és 'méret˝u' Koch fraktált. Hagyjuk a tekn˝ost ugyanabban az irányban.]

    Args:
        t ([type]): [description]
        rend ([type]): [description]
        meret ([type]): [description]
    """
    
    if rend == 0:           # Alapesetben csak egy egyenes
        t.forward(meret)
    else:
        for szog in [60, -120, 60, 0]:
            koch(t, rend-1, meret/3)
            t.left(szog)

def koch_0(t, meret):
    t.forward(meret)

def koch_1(t, meret):
    koch_0(t, meret/3)
    t.left(meret)

def koch_2(t, meret):
    for szog in [60, -120, 60, 0]:
        koch_1(t, meret/3)
        t.left(szog)

def koch_3(t, meret):
    for szog in [60, -120, 60, 0]
    koch_2(t, meret/3)
    t.left(szog)