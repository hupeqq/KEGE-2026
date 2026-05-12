for x in range(1, 500001):
    for p in range(11, 37):
        if int('29A1', p) + int('47771', p) + int('12A', p) == 1_000_000 + x:
            print(p)