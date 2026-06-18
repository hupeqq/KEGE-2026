with open('./files/27_A_29357.txt') as file:
    dots = []
    orange_giants = []
    yellow_dwarfs = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] >= '':
            orange_giants.append(list(map(float, [x, y])))