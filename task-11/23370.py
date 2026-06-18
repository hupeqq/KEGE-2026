from math import log2, ceil
for L in range(1, 10**10):
    n = 27
    i = ceil(log2(n))
    I = ceil(L * i / 8)
    if I * 7564230 > 31 * 2 **20:
        print(L)
        break