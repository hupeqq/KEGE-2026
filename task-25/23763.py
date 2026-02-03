def delit(x):
    D = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            D.add(d)
            D.add(x // d)
    return sorted(list(D))
num = 800001
cnt = 0
while cnt != 5:
    if len(delit(num)) > 0:
        if (delit(num)[0] + delit(num)[-1]) % 10 == 4:
            print(num, delit(num)[0] + delit(num)[-1])
            cnt += 1
    num += 1
