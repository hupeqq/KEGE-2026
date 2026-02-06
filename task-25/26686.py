def fact(num):
    d = []
    while num % 2 == 0:
        d.append(2)
        num //= 2
    i = 3
    while i * i < num:
        while num % i == 0:
            d.append(i)
            num //= i
        i += 2
    if num > 2:
        d.append(num)
    return d
cnt = 0
for n in range(89428305, 10**20):
    D = fact(n)
    if len(D) >= 6 and n % sum(D) == 0:
        cnt += 1
        print(n, sum(D))
        if cnt == 6:
            break
