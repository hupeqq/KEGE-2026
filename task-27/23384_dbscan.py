from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open(r'./files/27_A_23384.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
eps = 1
clusters1 = []
while dots:
    cluster1 = [dots.pop()]
    for dot in cluster1:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster1.append(d)
                dots.remove(d)
    clusters1.append(cluster1)
centers = [center(cluster) for cluster in clusters1]
print(sum(center[0] for center in centers) * 10000)
print(sum(center[1] for center in centers) * 10000)

with open(r'./files/27_B_23384.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
eps = 1
clusters2 = []
while dots:
    cluster2 = [dots.pop()]
    for dot in cluster2:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster2.append(d)
                dots.remove(d)
    if len(cluster2) > 10:
        clusters2.append(cluster2)
centers2 = [center(cluster) for cluster in clusters2]
print(min(dist(center, [0, 0]) for center in centers2) * 10000)
print(max(dist(center, [0, 0]) for center in centers2) * 10000)

