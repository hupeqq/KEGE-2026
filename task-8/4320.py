from itertools import permutations
from string import printable
cnt = 0
for val in permutations(printable[:8], 6):
    val = ''.join(val)
    if val[0] != '0' and str(int(val, 8))[-1] in '05':
        for i in val:
            if i in '0246':
                val = val.replace(i, '*')
            if i in '1357':
                val = val.replace(i, '#')
        if '**' not in val and '##' not in val:
            cnt += 1
print(cnt)
