# псевдослучайные числа

import random
# псевдослучайные числа от а до б
print(random.randint(1, 100))
# псевдослучайные числа от 0 до 1
print(random.random())

# псевдослучайный элемент из списка
arr = [1, 2, 3, 4]
print(random.choice(arr))

# n-псевдослучайных элементов из списка
arr2 = [1, 88, 44, 23, 987, 11, 2, 810, 1111]
n = 5
print(random.sample(arr2, n))
