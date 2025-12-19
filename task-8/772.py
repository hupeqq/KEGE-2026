from itertools import permutations
cnt = 0
alph = 'пробник'
for val in set(permutations(alph, 7)):
    val = ''.join(val)
    if val[0] not in 'ои' and val[-1] not in 'ои':
        if 'ио' not in val and 'ои' not in val:
            cnt += 1
print(cnt)