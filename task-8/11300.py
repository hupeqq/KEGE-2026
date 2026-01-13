from itertools import product
alph = sorted('ГОНДУБШ')
cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos %2 == 1 and val[0] != 'Б' and val.count('У') == 0 and val.count("Н") >= 2:
        print(pos)
