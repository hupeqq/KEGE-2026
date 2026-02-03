def delit(num):
    D = []
    for d in range(19, int(num / 2) + 1):
        if num % d == 0 and str(d)[-1] == '9':
            D.append(d)
    return D
num = 800001
cnt = 0
while cnt != 5:
    if len(delit(num)) != 0:
        print(num, delit(num)[0])
        cnt += 1
    num += 1