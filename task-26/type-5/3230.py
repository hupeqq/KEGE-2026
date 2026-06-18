with open('../files/26_3230.txt') as file:
    n = int(file.readline())
    trees = [list(map(int, i.split())) for i in file][:-1]
trees = sorted(trees, key=lambda x: (-x[0], x[1]))
for i in range(len(trees) - 1):
    if trees[i][0] == trees[i + 1][0]:
        if trees[i + 1][1] - trees[i][1] == 12:
            print(trees[i][0], trees[i][1] + 1)
            break