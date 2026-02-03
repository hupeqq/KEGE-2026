def delit(num):
    D = []
    for d in range(2, int(num // 2) + 1):
        if num % d == 0 and str(d)[-1] == '7' and d != 7:
            D.append(d)
            D.append(num // d)
    return D
num = 700001
cnt = 0
while cnt != 5:
    if len(delit(num)) > 0:
        print(num, delit(num)[0])
        cnt += 1
    num += 1

