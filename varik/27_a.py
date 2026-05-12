from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open('./files/1_27_A.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'M' and data[2:] == 'III':
            stars.append(list(map(float, [x, y])))
cluster1 = [d for d in dots if d[1] < 15]
cluster2 = [d for d in dots if d[1] > 15]
clusters = sorted([cluster1, cluster2], key=len)
center = center(clusters[0])
reds1 = [d for d in stars if d in cluster1]
mindist = 10 ** 10
ans = []
for d in reds1:
    if mindist > dist(d, center):
        mindist = dist(d, center)
        ans = d
print(ans[0] * 10000, ans[1] * 10000)
### 44694 69754