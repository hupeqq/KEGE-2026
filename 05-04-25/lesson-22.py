# перенаправление потока в файл
file = open('test.txt')

# считывание еще не считанной строки
print(file.readline())
# считывание еще не считанных строк
print(file.readlines())
# закрытие потока
file.close()