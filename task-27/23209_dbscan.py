from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open(r'./files/27_A_23209.txt') as file:
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
print(max(center[0] for center in centers) * 10000)
print(max(center[1] for center in centers) * 10000)
with open(r'./files/27_B_23209.txt') as file:
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
    if len(cluster2) > 1:
        clusters2.append(cluster2)
centers = [center(cluster) for cluster in clusters2]
mini = min(clusters2, key=len)
maxi = max(clusters2, key=len)
print((center(maxi)[0] - center(mini)[0]) * 10000)
print((center(maxi)[1] - center(mini)[1]) * 10000)
