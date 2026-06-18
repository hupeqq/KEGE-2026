with open('./files/26_9756.txt') as file:
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]
times = sorted(times, key=lambda x:(x[1], x[0]))
current = times[0][1]
ans = [current]
for i in times:
    if i[0] >= current:
        ans.append(i)
        current = i[1]
ans = ans[:-1]
for i in times[::-1]:
    if i[0] >= ans[-1][1]:
        ans.append(i)
        break
print(len(ans), ans[-1][1])