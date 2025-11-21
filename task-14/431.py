for x in range(1, 10000):
    num = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 7**(2*x)
    res = ''
    while num:
        res += str(num % 7)
        num //= 7
    if sum(map(int, res)) == 18:
        print(x)
        break