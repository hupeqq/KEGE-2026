from itertools import permutations
cnt = 0
alph = 'КИДАЛА'
for val in set(permutations(alph, 5)):
    val = ''.join(val)
    if 'АА' not in val:
        cnt += 1
print(cnt)
