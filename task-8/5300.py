from itertools import permutations
cnt = 0
alph = 'ХОЧУ В ВУЗ'
for val in set(permutations(alph, 10)):
    val = ''.join(val)
    if val[0] not in ' ' and val[-1] not in ' ' and val[0] != 'У' and ' У' not in val and '  ' not in val:
        cnt += 1
print(cnt)