from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open('./files/27_A_28946 (1).txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
clusters1 = []
eps = 3
while dots:
    cluster1 = [dots.pop()]
    for dot in cluster1:
        for d in dots.copy():
            if eps > dist(dot, d):
                cluster1.append(d)
                dots.remove(d)
    if len(cluster1) > 5:
        clusters1.append(cluster1)
centers1 = [center(cluster) for cluster in clusters1]
maxi1 = max(cluster for cluster in clusters1)
cent_max = center(maxi1)
A1 = sum(1 for dot in maxi1 if dot[1] < cent_max[1])
A2 = centers1[0][0] - centers1[1][0]
print(A1, A2 * 10000)

with open('./files/27_B_28946 (1).txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
clusters2 = []
eps = 1
while dots:
    cluster2 = [dots.pop()]
    for dot in cluster2:
        for d in dots.copy():
            if eps > dist(dot, d):
                cluster2.append(d)
                dots.remove(d)
    if len(cluster2) > 5:
        clusters2.append(cluster2)
clusters2 = sorted(clusters2, key=len)
centerB1 = center(clusters2[0])
B1 = sum(1 for dot in clusters2[0] if dist(dot, centerB1) < 0.9 * 2 ** 0.5)
B2 = center(clusters2[1])[1] - center(clusters2[2])[1]
print(B1, B2 * 10000)