def read_without(beolvas, fillout):
    """[Írj egy olyan programot, amely beolvas egy fájlt, és csak azokat a sorait írja ki, melyek tartalmazzák az info
részsztringet.]

    Args:
        beolvas ([type]): [description]
        fillout ([type]): [description]
    """
    for line in list(open(beolvas)):
        if fillout in line:
            print(line, end="")
      

read_without("text.txt", "info")