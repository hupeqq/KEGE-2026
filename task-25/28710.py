def f(num):
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
    count = 0
    if len(d) == 3:
        for i in d:
            if '3' in str(i) and '5' in str(i):
                count += 1
    if count == 3:
        return max(d)
    return 0

cnt = 0
num = 3600001
while cnt != 5:
   res = f(num)
   if res:
       print(num, res)
       cnt += 1
   num += 1