with open(r'.\files\17522.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    amount = [line.count(i) for i in line]
    if amount.count(2) == 2 and amount.count(1) == 2:
        if max(line) < sum(line) - max(line):
            cnt += 1
print(cnt)
