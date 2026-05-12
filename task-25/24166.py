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
    if str(sum(d)) == str(sum(d))[::-1]:
        return d
    return []
num = 7305679
cnt = 0
while cnt != 5:
    if fact(num) and len(fact(num)) == 4:
        print(num, sum(fact(num)))
        cnt += 1
    num += 1

