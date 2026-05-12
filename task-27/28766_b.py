with open('./files/27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:] == 'I':
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
yellow1 = [d for d in stars if d in cluster1]
yellow2 = [d for d in stars if d in cluster2]
yellow3 = [d for d in stars if d in cluster3]
for dot in yellow1:
    mini1 = min(dist(dot, d) for d in yellow1 if dot != d)
for dot in yellow3:
    mini3 = min(dist(dot, d) for d in yellow3 if dot != d)
print(min(mini1, mini3) * 10000)
centers = [center(cluster) for cluster in (cluster1, cluster2, cluster3)]
print(dist(centers[1], centers[2]) * 10000)


