def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    if sum(1 for i in d if str(i).count('6') == 1) == 2 and len(d) == 2:
        return d
    return 0
num = 6086056
cnt = 0
while cnt != 5:
    if res := fact(num):
        print(num, max(res))
        cnt += 1
    num += 1

