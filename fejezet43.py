def teglalap_rajzolas(t, sz, m):
    for i in range(2):
        t.forward(sz)
        t.left(90)
        t.forward(m)
        t.left(90)

def negyzet_rajzolas(tk, h):
    teglalap_rajzolas(tk, h, h)