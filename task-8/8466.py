from itertools import product
from string import printable
cnt = 0
for val in product(printable[:7], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and (val[-1] not in '0123'):
        for j in val:
            if j in '0246':
                val = val.replace(j, '*')
            if j in '1357':
                val = val.replace(j, '#')
        if val.count('*') == val.count('#'):
            cnt += 1
print(cnt)