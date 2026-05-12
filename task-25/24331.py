def fact(x):
    d = []
    while x % 2 == 0:
        d.append(2)
        x //= 2
    i = 3
    while i * i < x:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 2
    if x > 2:
        d.append(x)
    return d
cnt = 0
num = 13475125
while cnt != 5:
    if len(fact(num)) == 5 and all(str(i).count('5') for i in fact(num)):
        print(num, fact(num))
        cnt += 1
    num += 1

