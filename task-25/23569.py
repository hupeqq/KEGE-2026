def fact(num):
    d = []
    while num % 2 == 0:
        d.append(2)
        num //= 2
    i = 3
    while i * i < num + 1:
        while num % i == 0:
            d.append(i)
            num //= i
        i += 2
    if num > 2:
        d.append(num)
    return d
num = 6086056
cnt = 0
while cnt != 5:
    if len(fact(num)) == 2 and all(str(i).count('6') == 1 for i in fact(num)):
        print(num, max(fact(num)))
        cnt += 1
    num += 1

