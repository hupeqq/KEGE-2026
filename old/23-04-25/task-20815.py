with open("26_20815.txt") as file:
    N, K = map(int, file.readline().split())
    info = []
    for i in file:
        a1, a2, a3, a4, a5 = map(int, i.split())
        info.append([a2 + a3 + a4 + a5, a5, a1])
info.sort(key=lambda x:( -x[0], -x[1], x[2]))
cnt = 0
data = []
if info[K - 1][0] == info[K][0]:
    half_point = info[K][0]
    for i in info:
        if i[0] == half_point:
            cnt += 1
        if i[0] > half_point:
            data.append(i[2])
else:
    print(info[K - 1][2], 0)
print(data[-1])
print(cnt)
