with open('../files/26_23383.txt') as file:
    n = int(file.readline())
    sportsmen = [list(map(int, i.split())) for i in file]
sportsmen = sorted(sportsmen, key=lambda x: (x[1], x[0]))
cnt = 1
ans = []
for i in range(len(sportsmen) - 1):
    if sportsmen[i][1] == sportsmen[i + 1][1]:
        if sportsmen[i + 1][0] == sportsmen[i][0]:
            continue
        if sportsmen[i + 1][0] - sportsmen[i][0] == 1:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 1
    ans.append([cnt, sportsmen[i][1]])

ans = sorted(ans, key=lambda x: (x[0], -x[1]))
print(ans[-1])