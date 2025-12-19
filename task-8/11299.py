from itertools import product
alph = 'БМНРЮ'
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'М' and val.count('Р') >= 2 and val.count('Ю') == 0:
        print(pos)