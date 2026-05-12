with open('./files/27_B_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
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
stars1 = [d for d in stars if d in cluster1]
stars2 = [d for d in stars if d in cluster2]
stars3 = [d for d in stars if d in cluster3]
clusters = sorted([cluster1, cluster2, cluster3], key=len)
print(dist(center(clusters[0]), center(clusters[2])) * 10000)
dists = []
for s1 in stars1:
    for s2 in stars2:
        dists.append(dist(s1, s2))
for s1 in stars2:
    for s2 in stars3:
        dists.append(dist(s1, s2))
for s1 in stars1:
    for s2 in stars3:
        dists.append(dist(s1, s2))
print(max(dists) * 10000)