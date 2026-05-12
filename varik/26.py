with open('./files/1_26.txt') as file:
    n = int(file.readline())
    info = [list(map(int, i.split())) for i in file]

average = sum(i[1] for i in info) / n

expens = [i for i in info if i[1] > average]
cheap = [i for i in info if i[1] < average]

expens = sorted(expens, key=lambda x: (x[0], x[2]))
ans_sold = []
sold = 1
for i in range(len(expens) - 1):
    if expens[i][0] == expens[i + 1][0] and expens[i][2] == expens[i + 1][2] == 0:
        sold += 1
    elif expens[i][0] == expens[i + 1][0] and expens[i][2] != expens[i + 1][2]:
        ans_sold.append([expens[i][0], expens[i][1], sum(j[2] for j in expens if j[0] == expens[i][0]), sold])
        sold = 1
    elif expens[i][0] != expens[i + 1][0]:
        sold = 1
ans_sold = sorted(ans_sold, key=lambda x: (-x[3], -x[1], x[2]))
print(ans_sold[0][1] * ans_sold[0][3], ans_sold[0][2])
##### 43656 36