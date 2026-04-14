with open("26_9077.txt") as file:
    M, N = map(int, file.readline().split())
    scooters = []
    for i in file:
        scooters.append(list(map(int, i.split())))
scooters.sort()
parking= {}
for i in range(1, M + 1):
    parking[i] = []
cnt = 0
for i in scooters:
    parking[i[3]].append(i[0] + i[1])
    if len(parking[i[2]]) == 0:
        cnt += 1
    elif min(parking[i[2]]) >= i[0]:
        cnt += 1
    elif min(parking[i[2]]) < i[0]:
        parking[i[2]].remove(min(parking[i[2]]))
print(cnt)