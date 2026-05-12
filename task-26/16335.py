with open('files/26_16335.txt') as file:
    n = int(file.readline())
    korzhi = list(map(int, file.readlines()))
korzhi = sorted(korzhi, reverse=True)
big = korzhi[0]
ans = [big]
for korzh in korzhi:
    if big - korzh >= 4:
        ans.append(korzh)
        big = korzh
minim = 0
if ans[-1] >= korzhi[-1]:
    minim = korzhi[-1]
print(len(ans), minim)
