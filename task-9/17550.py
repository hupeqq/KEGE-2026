with open(r'.\files\17550.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    amount = [line.count(i) for i in line]
    if amount.count(3) == 3 and amount.count(1) == 3:
        pov = sum(i for i in line if line.count(i) == 3) ** 2
        nepov = sum(i for i in line if line.count(i) == 1) ** 2
        if pov > nepov:
            cnt += 1
print(cnt)