import random
num = random.randint(10000, 99999)
destys = num // 10000
tys = (num % 1000) // 1000
sot = (num // 1000) % 1000
des = (num // 10) % 10
ed = num % 10
print(num)
print(destys, tys, sot, des, ed)