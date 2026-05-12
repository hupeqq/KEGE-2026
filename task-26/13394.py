from math import floor
with open(r'./files/26.6_13394.txt') as file:
    n = int(file.readline())
    disc = []
    not_disc = []
    for i in file:
        if int(i) > 350:
            disc.append(int(i))
        else:
            not_disc.append(int(i))
disc = sorted(disc, reverse=True)
k = 3
sum_dif = sum(not_disc) + sum(disc) - sum(floor(i * 0.75) for i in disc[k - 1::k])
sum_one = sum(not_disc) + sum(disc) - floor(sum(disc[-len(disc) // k:])*0.75)
print(sum_dif, sum_one)