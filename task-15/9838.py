for a in range(1, 1000):
    k = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            k *= (x + 2*y > a) or (y < x) or (x < 30)
            if not k:
                break
        if not k:
            break
    else:
        print(a)