from math import dist
with open('./files/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            stars.append(list(map(float, [x, y])))
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]
quazars1 = [dot for dot in stars if dot in cluster1]
quazars2 = [dot for dot in stars if dot in cluster2]
center1 = center(cluster1)
center2 = center(cluster2)
dists = []
for s in quazars1:
    dists.append(dist(center1, s))
for s in quazars2:
    dists.append(dist(center2, s))
print(min(dists) * 10000, max(dists) * 10000)

