from itertools import permutations
cnt = 0
alph = 'ВОРОТА'
for val in set(permutations(alph, 6)):
    val = ''.join(val)
    if 'АО' not in val and 'ОО' not in val and 'ОА' not in val:
        cnt += 1
print(cnt)