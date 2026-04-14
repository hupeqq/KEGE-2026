with open("26_9171.txt") as file:
    M, K, N = map(int, file.readline().split())
    stations = {}
    for i in range(M):
        stations[i + 1] = []
    for i in file:
        start, end = map(int, i.split())
        stations[start].append(end)
cnt_passengers = 0
full_train = 0
seats = [0] * K
for i in stations:
    while i in seats:
        pos_left_person = seats.index(i)
        seats[pos_left_person] = 0
    stations[i].sort(reverse=True)
    for passenger in stations[i]:
        if 0 in seats:
            pos_free_place = seats.index(0)
            seats[pos_free_place] = passenger
            cnt_passengers += 1
        else:
            break
    if 0 not in seats:
        full_train += 1
print(cnt_passengers, full_train)