with open(r'.\files\9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]
for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in line]
    if amount.count(2) == 2 and amount.count(1) == 4:
        povt = [i for i in line if line.count(i) == 2]
        nepovt = [i for i in line if line.count(i) == 1]
        if sum(nepovt) / 4 <= sum(povt) / 2:
            print(pos)
            break
