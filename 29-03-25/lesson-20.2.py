# В цикле for метод remove лучше не использовать
# т.к. после удаления элемента из списка
# указатель итератора будет смещаться
# из-за чего мы не проверим все элементы списка

data = []
# Заполнение списка четными числами от 2 до 20
for i in range(2, 20, 2):
    data.append(i)

# Удаление четных чисел из списка
for i in data:
    if i % 2 == 0:
        data.remove(i)

# В списке остались четные числа,
# т.к. remove не позволил итератору пройти по всем элементам
print(data)
