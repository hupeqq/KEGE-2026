from itertools import permutations
cnt = 0
alph = 'АМФИБРАХИЙ'
for val in set(permutations(alph, r=len(alph))):
    val = ''.join(val)
    if val[5:7] == 'БР':
        cnt += 1
print(cnt)