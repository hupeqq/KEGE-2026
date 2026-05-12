from itertools import permutations
alph = 'ТИХОРЕЦК'
cnt = 0
cnt_ans = 0
for val in permutations(alph, 4):
    val = ''.join(val)
    if val.count('И') + val.count('О') + val.count('Е') == 2:
        for i in range(len(val)):
                if 'ТИХО'[i] == val[i]:
                    cnt += 1
        if cnt == 2:
            cnt_ans += 1
        cnt = 0
print(cnt_ans)


