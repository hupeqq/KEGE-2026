with open('./files/26_23208.txt') as file:
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]
    res = []
    for i in range(len(times)):
        res.append(sorted([[times[i][0], 0], [times[i][1], 1]]) + [i + 1])
res = sorted(res)
cnt = 0
last = res[-1]
for i in res:
    if i[0][1] == 0:
        if last[1][0] > i[0][0]:
            cnt += 1
print(last[-1], cnt)
