data = input("Введите вашу строку: ")
symbol = input("Введите символ который нужно удалить: ")
while data[0] == symbol:
    data = data[1:]
while data[-1] == symbol:
    data = data[:-1]
print(data)



