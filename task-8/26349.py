from itertools import product
alph = sorted('СУЛАК')
maxi = 0
for i in range(1, 10):
    for pos, val in enumerate(product(alph, repeat=i), start=1):
        val = ''.join(val)
        if val[0] in 'ЛС' and pos % 2 == 0:
            for j in val:
                if j in 'АУ':
                    val = val.replace(j, '*')
            if val.count("*") <= 2 and '**' not in val:
                maxi = max(maxi, pos)
    if maxi == 12368:
        print(i)
    else:
        maxi = 0