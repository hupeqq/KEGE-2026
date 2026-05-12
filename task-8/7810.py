from itertools import product
alph = sorted('МАСЛО')
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val.count('А') + val.count('О') == 1:
        cnt += 1
print(cnt)