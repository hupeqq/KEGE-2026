with open(r'.\files\9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in line]
    if amount.count(3) == 3 and amount.count(1) == 4:
        sr = sum(i for i in line if line.count(i) == 1) / 4
        nepovt = sum(i for i in line if line.count(i) == 3) / 3
        if nepovt >= sr:
            cnt += 1
print(cnt)