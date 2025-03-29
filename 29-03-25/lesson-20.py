#Коллекции включают в себя:
#Последовательности-str list tuple
#Множество-set
#Словарь-dict

#цикл for создает итератор и перебирает элементы списка
# data - список(итерируемый объект)
data = [1, 2, 3]
for i in data:
    print(i)

data = [1, 2, 3]
# под капотом цикл for выполняет следующие действия:
my_iter = iter(data)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
