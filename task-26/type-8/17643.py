from pprint import pformat

with open('../files/26_17643.txt') as file:
    n = int(file.readline())
    info = [list(map(int, i.split())) for i in file]
average = sum(i[1] for i in info) / len(info)
leaders = [i for i in info if i[1] > average]
res = []
leaders = sorted(leaders)
for i in range(len(leaders)):
    art = leaders[i][0]
    cost = leaders[i][1]
    res.append([art, sum(1 for i in leaders if i[2] == 1 and art == i[0]), sum(1 for i in leaders if i[2] == 0 and art == i[0]), cost])
only_res = []
for i in res:
    if i not in only_res:
        only_res.append(i)
    else:
        continue
only_res = sorted(only_res, key=lambda x: (-x[2], -x[3], x[1]))
print(only_res[0][2] * only_res[0][3], only_res[0][1])