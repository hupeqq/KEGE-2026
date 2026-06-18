with open(r'.\files\23268.txt') as file:
    data = [list(map(int, i.split())) for i in file]
for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in line]
    if amount.count(2) == 4 and amount.count(1) == 3:
        maxi = max(i for i in line if line.count(i) == 1)
        povt = sum(i for i in line if line.count(i) == 2) / 4
        if maxi > povt:
            print(pos)
            break