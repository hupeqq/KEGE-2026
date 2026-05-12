with open('./files/27_B_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y':
            stars.append(list(map(float, [x, y])))
from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
cluster1 = [d for d in dots if d[1] > 23]
cluster2 = [d for d in dots if d[1] < 23 and d[1] > 15]
cluster3 = [d for d in dots if d[1] < 15]
red1 = [dot for dot in stars if dot in cluster1]
red2 = [dot for dot in stars if dot in cluster2]
red3 = [dot for dot in stars if dot in cluster3]
if len(red3) > len(red1) > len(red2):
    print(dist(center(cluster3), center(cluster2)) * 10000)
