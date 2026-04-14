with open('26_19752.txt') as file:
    N = int(file.readline())
    info = []
    for i in file:
        data = list(map(int, i.split()))
        summ = sum(data[1:])
        plus = sum([j for j in data[1:] if j > 0])
        ans = 10 - data[1:].count(0)
        info.append([data[0], summ, plus, ans])
info.sort(key=lambda x:(-x[1], -x[2], -x[3], x[0]))
cnt = 0
for i in info[N // 3:]:
        if info[N // 3 - 1][1:] == i[1:]:
            cnt += 1
info = info[N // 3 + cnt:]
id_winner = info[0][0]
losers = []
for i in info[N // 3 + cnt:]:
    if i[1] > 0:
        losers.append(i)
losers = losers[len(losers) // 10]
for i in info[N // 3 + cnt:]:
        if losers[-1][1:] == i[1:]:
            losers.append(i)
print(id_winner, len(losers))