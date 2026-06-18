with open('../files/26_21598.txt') as file:
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]
timeline = [0] * 1441
for start, end in times:
    for i in range(start, end):
        timeline[i] += 1
cnt = 1
ans = 0
for i in range(len(timeline) - 1):
    if timeline[i] == timeline[i + 1]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
diff = 1
timeline = sorted(timeline, reverse=True)
for i in range(1, len(timeline) - 1):
    if timeline[i] != timeline[i + 1]:
        diff += 1
    if diff == 2:
        print(1440 - i - 1)
        break
print(ans)