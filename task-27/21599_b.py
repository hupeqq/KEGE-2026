from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open('./files/27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster1 = [dot for dot in dots if dot[1] < -5]
cluster2 = [dot for dot in dots if -5 < dot[1] < dot[0]]
cluster3 = [dot for dot in dots if dot[0] < dot[1] < 10/7 * dot[0] + 10]
cluster4 = [dot for dot in dots if 7*(dot[1] - 10)/ 10 > dot[0] > -10]
cluster5 = [dot for dot in dots if -10 > dot[0] > (dot[1] + 19)*12/-19]
cluster6 = [dot for dot in dots if dot[0] < (dot[1] + 19)*12/-19]
centers = [center(cluster) for cluster in (cluster1, cluster2, cluster3, cluster4, cluster5, cluster6)]
print(sum(center[0] for center in centers) / 6 * 10000)
print(sum(center[1] for center in centers) / 6 * 10000)