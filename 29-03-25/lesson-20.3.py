# заполнить список двадцатью случайными числами
from random import randint
data = []
for i in range(20):
    data.append(randint(-100, 100))
print(data)


otrits = 0
polozh = 0
for i in data:
    if i >= 0:
        polozh += 1
    else:
        otrits += 1
print(polozh, otrits)


