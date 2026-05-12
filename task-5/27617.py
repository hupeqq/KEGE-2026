ans = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin(n * 3)[2:]
    res = int(r, 2)
    ans.append([n, res])
minim = 10000
maxim = 0
for i in ans:
    minim =  abs(min(i[1] - 130, minim))
for i in ans:
    if i[1] == 130 - minim:
        maxim = max(maxim, i[0])
print(maxim)
print(ans)