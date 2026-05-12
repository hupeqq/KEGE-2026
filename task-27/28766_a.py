with open('./files/27_A_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y' and data[2:] == 'III':
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
mini = min(cluster2, cluster1, key=len)
centerr = center(mini)
maxi = max(dist(dot, centerr) for dot in stars)
mini = min(dist(dot, centerr) for dot in stars)
print(mini * 10000)
print(maxi * 10000)