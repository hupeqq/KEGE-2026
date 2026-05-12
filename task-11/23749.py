from math import *
for n in range(1, 1000000):
    l = 2783
    i = ceil(log2(n))
    I = ceil(l * i / 8)
    if I * 3845627 >= 11 * 2 ** 30:
        print(n)
        break