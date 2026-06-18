ans = []
for n in range(4, 4000):
    num = '1' + '2' * n
    while '12' in num or '322' in num or '2222' in num:
        if '12' in num:
            num = num.replace('12', '2', 1)
        if '322' in num:
            num = num.replace('322', '21', 1)
        if '2222' in num:
            num = num.replace('2222', '3', 1)
    ans.append(num.count('1')  + num.count('2') * 2 + num.count('3') * 3)
print(max(ans))