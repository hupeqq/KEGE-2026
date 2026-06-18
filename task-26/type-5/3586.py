with open('../files/26_3586.txt') as file:
    n = int(file.readline())
    trees = [list(map(int, i.split())) for i in file][:-1]
trees = sorted(trees, key=lambda x: (-x[0], x[1]))
ans_row = 0
ans_seats = 0
for i in range(len(trees) - 1):
    if trees[i][0] == trees[i + 1][0]:
        if trees[i + 1][1] - trees[i][1] - 1 > ans_seats:
            ans_row = trees[i][0]
            ans_seats = trees[i + 1][1] - trees[i][1] - 1
print(ans_row, ans_seats)