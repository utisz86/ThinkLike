def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t

import time
t0 = time.process_time()
n = 35
eredmeny = fib(n)
t1 = time.process_time()


print("fib({0}) = {1}, ({2:.2f} masodperc)".format(n, eredmeny, t1-t0))