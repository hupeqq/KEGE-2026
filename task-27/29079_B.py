from math import dist
with open('./files/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'J' and data[2:] == 'V':
            stars.append(list(map(float, [x, y])))
cluster1 = [d for d in dots if d[1] > 23]
cluster2 = [d for d in dots if d[1] < 23 and d[1] > 15]
cluster3 = [d for d in dots if d[1] < 15]
stars1 = [d for d in stars if d[1] > 23]
stars2 = [d for d in stars if d[1] < 23 and d[1] > 15]
stars3 = [d for d in stars if d[1] < 15]
clusters = sorted([cluster1, cluster2, cluster3], key=len)
print(max(dot[0] for dot in stars3) * 10000)
print(max(dot[1] for dot in stars1) * 10000)