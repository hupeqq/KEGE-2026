with open(r'.\files\23193.txt') as file:
    data = [list(map(int, i.split())) for i in file]
for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in line]
    if amount.count(3) == 3 and amount.count(1) == 3:
        pov = sum(i for i in line if line.count(i) == 3) / 3
        nepov = sum(i for i in line if line.count(i) == 1) / 3
        if pov > nepov:
            print(pos)