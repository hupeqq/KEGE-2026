with open('26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = []
    for i in file:
        times.append(list(map(int, i.split())))
cells = [0] * K
cnt = 0
last = 0
times = sorted(times)
for clients in times:
    for i in range(K):
        if cells[i] <= clients[0]:
            cells[i] = clients[1] + 1
            cnt += 1
            last = i + 1
            break
print(cnt, last)
