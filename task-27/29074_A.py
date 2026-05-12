with open('./files/27_A_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z':
            stars.append(list(map(float, [x, y])))
from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]
yellow1 = [d for d in stars if d in cluster1]
yellow2 = [d for d in stars if d in cluster2]
print(len(min(yellow1, yellow2, key=len)))
print(len(max(yellow1, yellow2, key=len)))