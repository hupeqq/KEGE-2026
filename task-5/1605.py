ans = []
for n in range(1, 100000):
    r = bin(n + 2)[2:]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    res = int(r, 2)
    if res < 61:
        ans.append([n, res])
print(max(ans))

