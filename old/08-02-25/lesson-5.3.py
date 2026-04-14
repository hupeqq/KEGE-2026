num1 = 70
num2 = 100
num3 = 64

f1 = num1 % num2 == 0 # False
f2 = num2 + num3 > num1 #True
f3 = num3 % 2 == 0 # True

if f1 and f2: # False and True = False
    print('Test1')

if f2 and f3 and f1: # True and True and False = False
    print('Test2')

if f1 or f2: # False or True = True
    print('Test1')

if f1 or not f2: # False or not True = False
    print('Test1')

if f1 or not f2 and f3: # False or not True and True = False
    print('Test1')


