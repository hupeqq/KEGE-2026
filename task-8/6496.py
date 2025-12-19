from itertools import product
alph = 'БЕРСК'
cnt = 0
for i in range(5, 8):
    for val in product(alph, repeat=i):
        val = ''.join(val)
        cnt += 1
print(cnt)