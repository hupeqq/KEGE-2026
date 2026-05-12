from itertools import product
alph = sorted('КРАТЕ')
cnt_1 = 0
cnt_2 = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'КАРЕТА':
        cnt_1 = pos
    elif val == 'РАКЕТА':
        cnt_2 = pos
print(cnt_2 - cnt_1 - 1)
