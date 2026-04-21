from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open('./files/27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster1 = [dot for dot in dots if dot[1] < -6]
cluster2 = [dot for dot in dots if -6 < dot[1] < 10/12 * dot[0] - 10]
cluster3 = [dot for dot in dots if dot[1] > 10/12 * dot[0] - 10]
centers = [center(cluster) for cluster in (cluster1, cluster2, cluster3)]
print(sum(center[0] for center in centers) / 3 * 10000)
print(sum(center[1] for center in centers) / 3 * 10000)

