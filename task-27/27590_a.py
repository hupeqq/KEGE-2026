from math import dist
def anticenter(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]
with open('./files/27A_27590.txt') as file:
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
mini1 = min(clusters1, key=len)
maxi1 = max(clusters1, key=len)
anticenters = [anticenter(cluster) for cluster in (mini1, maxi1)]
print((anticenters[0][0] + anticenters[0][1]) * 10000)
print((anticenters[1][0] + anticenters[1][1]) * 10000)
with open('./files/27B_27590.txt') as file:
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
    if len(cluster2) > 5:
        clusters2.append(cluster2)
anticenters2 = [anticenter(cluster) for cluster in clusters2]
maxi2 = max(dist((0, 0), anticenter) for anticenter in anticenters2)
mini2 = min(dist((0, 0), anticenter) for anticenter in anticenters2)
for i in anticenters2:
    if maxi2 == dist(i, [0, 0]):
        print(i[0] * 10000)
    if mini2 == dist(i, [0, 0]):
        print(i[1] * 10000)