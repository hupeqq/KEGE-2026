def delit(x):
    D = set()
    for d in range(2, int(x * 0.5) + 1):
        if x % d == 0 and d % 2 == 1:
            D.add(d)
    return sorted(list(D))
for x in range(18782, 18823):
    if len(delit(x)) == 3:
        print(delit(x))
