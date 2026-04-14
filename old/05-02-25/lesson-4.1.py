# подключение библиотеки
import random
print(random.randint(1,10))

# подключение библиотеки через псевдоним
import random as r
print(r.randint(1, 100))

# подключение одной команды (randint) из библиотеки
from random import randint
print(randint(1, 1000))

# подключение всех команд (randint) из библиотеки
from random import *
print(randint(-1010, 1111))



