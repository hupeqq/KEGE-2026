from itertools import product
alph = sorted('АРГУМЕНТ')
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    cnt = 0
    if len(set(val)) == len(val):
        for i in range(len(val) - 1):
            if val[i] <= val[i + 1]:
                cnt += 1
        if cnt == 3:
            print(pos)


