with open(r'.\files\23268.txt') as file:
    data = [list(map(int, i.split())) for i in file]
for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in line]
    if amount.count(2) == 4 and amount.count(1) == 3:
        pov = sum(i for i in line if line.count(i) == 2) / 4
        nepov = [i for i in line if line.count(i) == 1]
        if pov < max(nepov):
            print(pos)
            break