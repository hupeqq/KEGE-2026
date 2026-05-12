from math import dist
with open('./files/27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '3' and data[0] == 'L':
            stars.append(list(map(float, [x, y])))
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]
blue1 = [dot for dot in stars if dot in cluster1]
blue2 = [dot for dot in stars if dot in cluster2]
mini = min(cluster1, cluster2, key=len)
maxi = max(cluster1, cluster2, key=len)
dists1 = []
for dot in stars:
    dists1.append(dist(dot, center(mini)))
dists2 = []
for dot in stars:
    dists2.append(dist(dot, center(maxi)))
print(max(dists1) * 10000, max(dists2) * 10000)