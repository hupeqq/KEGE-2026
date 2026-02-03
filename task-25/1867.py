def delit(num):
    D = []
    for d in range(9, int(num / 2) + 1):
        if num % d == 0 and str(d)[-1] == '8':
            D.append(d)
    return D
num = 500001
cnt = 0
while cnt != 5:
    if len(delit(num)) != 0:
        print(num, delit(num)[0])
        cnt += 1
    num += 1

