from itertools import product
alph = sorted('НОРМАЛЬЕ')
cnt1 = 0
cnt2 = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'НЕНОРМ':
        cnt1 = pos
    elif val[:4] == 'НОРМ':
        cnt2 = pos
        break
print(cnt2 - cnt1 - 1)