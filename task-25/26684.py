def fact(num):
    d = []
    while num % 2 == 0:
        d.append('2')
        num //= 2
    i = 3
    while i * i < num + 1:
        while num % i == 0:
            d.append(str(i))
            num //= i
        i += 2
    if num > 2:
        d.append(str(num))
    return d
num = 5000012
cnt = 0
while cnt != 5:
    res = fact(num)
    if any(res.count(i) == 5 for i in set(res)):
        print(num, min(i for i in set(res) if res.count(i) == 5))
        cnt += 1
    num += 100
