from math import *

for n in range(1, 10 ** 8):
    l = 172
    i = ceil(log2(n))
    I = ceil(i * l / 8)
    if 356984 * I >= 54 * 2 ** 20:
        print(n)
        break
