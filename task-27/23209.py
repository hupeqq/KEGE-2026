from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open(r'./files/27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster_1 = [dot for dot in dots if dot[0] < 5]
cluster_2 = [dot for dot in dots if dot[0] > 5]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

print(max(center_1[0], center_2[0]) * 10000)
print(max(center_1[1], center_2[1]) * 10000)

with open(r'./files/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster_3 = [dot for dot in dots if 5 < dot[1] < 10]
cluster_4 = [dot for dot in dots if 16 < dot[1] < 21]
cluster_5 = [dot for dot in dots if 21 < dot[1] < 26]
mini = min(cluster_3, cluster_4, cluster_5, key=len)
maxi = max(cluster_3, cluster_4, cluster_5, key=len)
print((center(maxi)[0] - center(mini)[0]) * 10000)
print((center(maxi)[1] - center(mini)[1]) * 10000)