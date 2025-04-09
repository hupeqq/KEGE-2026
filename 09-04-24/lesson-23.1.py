with  open('26_7626.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    times = []
    for i in file:
        times.append(list(map(int, i.split())))
cells = [0] * k
cnt = 0
last = 0
times = sorted(times)
for clients in times:
    for i in range (k):
        if clients[0] >= cells[i]:
            cells[i] = clients[1] + 1
            cnt += 1
            last = i + 1
            break
print(cnt, last)