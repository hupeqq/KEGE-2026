for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 5 == 0:
        r += r[-3:]
    else:
        r += bin((n % 5) * 5)[2:]
    if int(r, 2) > 256:
        print(n)
        break
