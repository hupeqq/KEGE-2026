from itertools import product
from string import printable
cnt = 0
for val in product(printable[:7],repeat = 5):
    val = ''.join(val)
    if (val[0] != '0' and (val.count('3') + val.count('4') +  val.count('5')) == 2
            and all(val[j] != val[j + 1] for j in range(4))):
        cnt += 1
print(cnt)