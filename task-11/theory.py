#1855
from math import *
L = 101
N= 10 + 4090
i = ceil(log2(N))
I = ceil(L * i / 8)
print(2048 * I / 2**10)
#23270
for L in range(1, 10**9):
    N= 10 + 27
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 3548 * I > 12 * 2 ** 10:
        print(L)
        break