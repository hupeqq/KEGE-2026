from itertools import product
from string import printable
cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in val:
            if int(i, 12) % 3 == 0:
                val = val.replace(i, '*')
            else:
                val = val.replace(i, '#')
        if val == '#*#*#*#' or val == '*#*#*#*':
            cnt += 1
print(cnt)