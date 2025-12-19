from itertools import product

alph = sorted('сублимаця')
alph_1 = 'уиая'
for pos,val in enumerate(product(alph, repeat = 5), start=1):
    val = ''.join(val)
    if val[-1] != 'я' and pos % 2 == 1:
        cnt_1 = sum(1 for i in val if i in alph_1)
    if cnt_1 == 2:
        print(max(cnt_1, pos))