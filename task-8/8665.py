from itertools import product
from string import printable
cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val.count('b') == 2:
        for i in val:
            if i in '13579b':
                val = val.replace(i, '*')
            else:
                val = val.replace(i, '#')
        if val == '*#*#*#*' or val == '#*#*#*#':
            cnt += 1
print(cnt)
