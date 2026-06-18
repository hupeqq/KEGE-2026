with open('../files/26_1207.txt') as file:
    s, n = map(int, file.readline().split())
    vols = [int(i) for i in file]
vols = sorted(vols)
ans = []
for vol in vols:
    if s - vol > 0:
        s -= vol
        ans += [vol]
        last = vol
maxi = 0
for i in vols:
    if s + last > i:
        maxi = max(maxi, i)
print(len(ans), maxi)