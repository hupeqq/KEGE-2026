from itertools import product
alph = sorted('АЛГОРИТМ')
cnt = 0
for pos, val in enumerate(product(alph, repeat =6), start=1):
    val = ''.join(val)
    if val.count('Л') <= 1 and val[0] != 'Р' and val[-1] not in 'ЛГРТМ':
        cnt += 1
print(cnt)