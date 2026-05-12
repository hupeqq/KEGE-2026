from itertools import product
from string import printable
alph = printable[:25]
ans = 0
for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        if sum(1 for i in val if int(i, 25) > 15) > 2:
            for i in val:
                if int(i, 25) % 2 == 0:
                    val = val.replace(i, '*')
            if val.count('*') >= 1:
                ans += 1
print(ans)