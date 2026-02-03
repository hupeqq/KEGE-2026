def delit(num):
    D = []
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            D.append(d)
            D.append(num // d)
    return sorted(D)
num = 800001
cnt = 0
while cnt != 5:
    if len(delit(num)) != 0:
        if (delit(num)[0] + delit(num)[-1]) % 10 == 4:
            print(num, delit(num)[0] + delit(num)[-1])
            cnt += 1
    num += 1