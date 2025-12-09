from itertools import product
alph = sorted('ДИОНСЙ')
cnt = 0
for pos, val in enumerate(product(alph, repeat =6), start=1):
    val = ''.join(val)
    if 'Д' in val and 'Н' not in val or 'Н' in val and 'Д' not in val:
        if 'ДД' not in val and 'ИИ' not in val and 'ОО'not in val and 'НН' not in val and 'СС' not in val and 'ЙЙ' not in val:
            cnt += 1
            print(val)
print(cnt)