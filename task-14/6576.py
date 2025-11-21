num = 283 ** 382 + 9**15 + 2**3
res = ''
cnt_c = 0
cnt_b = 0
while num:
    if num % 14 == 11:
        cnt_b += 1
    elif num % 14 == 12:
        cnt_c += 1
    num //= 14
print(abs(cnt_c - cnt_b))