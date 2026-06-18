from math import log2, ceil
for l in range(1, 10**10):
    n = 37
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if I * 3548 > 12 * 2 **10:
        print(l)
        break