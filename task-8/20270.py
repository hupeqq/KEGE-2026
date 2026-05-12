from itertools import product
from string import printable
alph = printable[:7]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in val:
            if int(i) % 2 == 0:
                val = val.replace(i, '*')
        if val.count('**') >= 2 and val.count('***') == 0:
            cnt += 1
print(cnt)