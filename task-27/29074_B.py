with open('./files/27_B_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:] == 'V':
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
centers = [center(cluster) for cluster in (cluster1, cluster2, cluster3)]
blue1 = [d for d in stars if d in cluster1]
blue2 = [d for d in stars if d in cluster2]
blue3 = [d for d in stars if d in cluster3]
mini2 = min(dist(centers[1], d) for d in blue2)
mini3 = min(dist(centers[2], d) for d in blue3)
print(min(mini2, mini3) * 10000)
maxi2 = max(dist(centers[1], d) for d in blue2)
maxi3 = max(dist(centers[2], d) for d in blue3)
print(max(maxi2, maxi3) * 10000)
