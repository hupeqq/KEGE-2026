from random import randint
data = []
for i in range (20):
    data.append(randint(0, 9))
print(data)
summa = 0
kol_vo = 0
for i in data:
    summa += i
    kol_vo += 1
sr_ar = summa / kol_vo
print(sr_ar)
for i in data:
    if i < sr_ar:
        print(i)
