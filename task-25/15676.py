from fnmatch import fnmatch
#def f(num):
    #for i in range(2, int(num ** .5) + 1):
        #if num % i == 0:
            #return True
    #return False
#for num in range(22768, 10**8 + 1, 22768):
    #for sost in range(4, 1000):
        #if f(sost) and fnmatch(str(num), f'1{sost}03*6*'):
            #print(num, sost)

####################
from itertools import product
def f(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return True
    return False
ans = []
for l1 in range(5):
    for n in range(10 ** (l1 - 1), 10 ** l1):
        for l2 in range(0, 5 - l1):
            for z1 in product('0123456789', repeat=l2):
                z1 = ''.join(z1)
                for l3 in range(0, 5 - l1 - l2):
                    for z2 in product('0123456789', repeat=l3):
                        z2 = ''.join(z2)
                        num = int(f'1{n}03{z1}6{z2}')
                        if num % 22768 and num < 10 ** 8:
                            ans.append([num, n])
for i in sorted(ans):
    print(*i)
