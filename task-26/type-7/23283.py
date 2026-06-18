with open('../files/26_23283.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    clients = sorted([list(map(int, i.split())) for i in file])
cnt = 0
last = 0
windows = [0] * k
for start, end in clients:
    for i in range(len(windows)):
        if start >= windows[i] + 1:
            windows[i] = end
            cnt += 1
            last = i + 1
            break
print(cnt, last)