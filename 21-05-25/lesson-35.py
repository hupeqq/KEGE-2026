with open('26_21598 (2).txt') as file:
    N = int(file.readline())
    office = []
    for i in file:
        office.append(list(map(int, i.split())))

office.sort()
timeline = [0] * 1441
for i in office:
    for j in range(i[0], i[1]):
        timeline[j] += 1
changes = []
cnt = 1
ans = 0
for i in range(len(timeline) - 1):
    if timeline[i] == timeline[i + 1]:
        cnt += 1
    else:
        changes.append(i + 1)
        cnt = 1
    if cnt > ans:
        ans = cnt
print(changes[-2], ans)

