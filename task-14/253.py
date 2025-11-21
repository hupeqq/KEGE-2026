for n in range(1, 1000):
    num = 41
    num2 = 131
    res1 = ''
    res2 = ''
    while num:
        res1 += str(num % n)
        num //= n
    while num2:
        res2 += str(num2 % n)
        num2 //= n
    if res1[-1] == '2' and res2[-1] == '1':
        print(n)


