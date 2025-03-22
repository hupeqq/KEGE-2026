from timeit import timeit


def check_file_type_1(data):
    if data[-4:] == ".txt":
        print("Tекстовый файл")
    elif data[-4:] == ".jpg":
        print("Изображение")
    elif data[-4:] == ".png":
        print("Изображение")
    else:
        print("Неизвестный файл")


def check_file_type_2(data):
    if data.endswith(".txt"):
        print("Tекстовый файл")
    elif data.endswith(".jpg"):
        print("Изображение")
    elif data.endswith(".png"):
        print("Изображение")
    else:
        print("Неизвестный файл")


def check_file_type_3(data):
    if ".txt" in data:
        print("Tекстовый файл")
    elif ".jpg" in data:
        print("Изображение")
    elif ".png" in data:
        print("Изображение")
    else:
        print("Неизвестный файл")


st = 'sdhjvjhsdfbjhsdfkjsdvfjgsdkfjsdbjfvdsjkvnsdkufvshbfnkdslfysdvfhdnvisdvfgsdvjsbvfdsvfhjs.pngggh'
time1 = timeit('check_file_type_1(st)', globals=globals(), number=100)
time2 = timeit('check_file_type_2(st)', globals=globals(), number=100)
time3 = timeit('check_file_type_3(st)', globals=globals(), number=100)

print(time1, time2, time3)
