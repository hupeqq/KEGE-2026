with open('./files/26_23283.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]
windows = [0] * k
cnt = 0
last = 0
times = sorted(times)
for clients in times:
    for i in range(k):
        if windows[i] <= clients[0]:
            windows[i] = clients[1] + 1
            cnt += 1
            last = i + 1
            break
print(cnt, last)