from string import printable
from itertools import product
alph = printable[:7]
cnt = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] not in '035' and ('22' not in val or '44' not in val):
        cnt += 1
print(cnt)