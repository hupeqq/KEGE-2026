from string import printable
from itertools import product
alph = printable[:9]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in '1357':
            val = val.replace(i, '*')
        if val.count('0') == 1 and '*0' not in val and '0*' not in val:
            print(val)
            cnt += 1
print(cnt)