with open('./files/27_B_29076.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'J':
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
green1 = [dot for dot in stars if dot in cluster1]
green2 = [dot for dot in stars if dot in cluster2]
green3 = [dot for dot in stars if dot in cluster3]
mindist12 = 10**10
mindist23 = 10**10
mindist31 = 10**10
maxdist12 = 0
maxdist23 = 0
maxdist31 = 0
for dot in green1:
    for d in green2:
        mindist12 = min(mindist12, dist(dot, d))
for dot in green2:
    for d in green3:
        mindist23 = min(mindist23, dist(dot, d))
for dot in green1:
    for d in green3:
        maxdist31 = max(maxdist31, dist(dot, d))
print(min(mindist12, mindist23, mindist31) * 10000)
print(max(maxdist12, maxdist23, maxdist31) * 10000)