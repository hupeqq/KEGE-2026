from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open ('./files/27A_18677.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
clusters1 = []
eps = 1
while dots:
    cluster1 = [dots.pop()]
    for dot in cluster1:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster1.append(d)
                dots.remove(d)
    if len(cluster1) > 5: clusters1.append(cluster1)
centers = [center(cluster) for cluster in clusters1]
print((centers[0][0] + centers[1][0]) * 50000)
print((centers[0][1] + centers[1][1]) * 50000)
with open ('./files/27B_18677.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
clusters2 = []
eps = 1
while dots:
    cluster2 = [dots.pop()]
    for dot in cluster2:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster2.append(d)
                dots.remove(d)
    if len(cluster2) > 5: clusters2.append(cluster2)
centers2 = [center(cluster) for cluster in clusters2]
print(sum(center[0] for center in centers2) / 3 * 100000)
print(sum(center[1] for center in centers2) / 3 * 100000)