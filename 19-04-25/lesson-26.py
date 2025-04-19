with open('26.3_19890.txt') as file:
    N, M = map(int, file.readline().split())
    weights = []
    for i in file:
        weights.append(int(i))
weights.sort()
info = []
for i in weights:
    if sum(info) + i <= M:
        if 310 <= i <= 320:
            info.append(i)
for i in weights:
    if sum(info) + i <= M:
        if i < 310 or i > 320:
            info.append(i)
for i in weights:
    if info[-1] < i and i + sum(info[:-1]) <= M:
        info.remove(info[-1])
        info.append(i)
print(len(info), sum(info))


