with open(r'./files/14251.txt') as file:
    data = [list(map(int, i.split())) for i in file]
for line in data:
    amount = [line.count(i) for i in line]
    if amount.count(2) == 4 and amount.count(1) == 3:
        pov = sum(i for i in line if line.count(i) == 2)
        nech = sum(i for i in line if i % 2 == 1)
        if pov <= nech:
            print(sum(line))
