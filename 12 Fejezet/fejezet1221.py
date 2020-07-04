import time

def sajat_szum(xs):
    szum = 0
    for v in xs:
        szum += v
    return szum

sz = 10000000 # Legyen 10 millió eleme a listának
testadat = range(sz)

t0 = time.process_time()
sajat_eredmeny = sajat_szum(testadat)
t1 = time.process_time()
print("saját_eredmény = {0} (eltelt ido = {1:.4f} másodperc)".format(sajat_eredmeny, t1-t0))
t2 = time.process_time()
gepi_eredmeny = sum(testadat)
t3 = time.process_time()
print("gépi_eredmény = {0} (eltelt id˝o = {1:.4f} másodperc)".format(gepi_eredmeny, t3-t2))