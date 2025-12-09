from itertools import product
alph = sorted('ПОЛИНА')
cnt = 0
for pos, val in enumerate(product(alph, repeat = 8), start=1):
    val = ''.join(val)
    if val.count('П')+val.count('Л')+val.count('Н') > val.count('И')+val.count('А')+val.count('О'):
        cnt += 1
print(cnt)
