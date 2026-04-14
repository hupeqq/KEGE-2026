# Словарь - тип коллекций, которых хранит в себе неиндексированный итерируемый
# набор элементов в формате "ключ:значение".
# Словари являются отдельным типом коллекций,
# который называется отображением (mapping).
my_dict = {"name":"Ivan", "age":16}
print(my_dict["name"])
# keys - все ключи словаря
print(my_dict.keys())
# values - все значения словаря
print(my_dict.values())
# items - все связки
print(my_dict.items())

# извлечение элемента по ключу
print(my_dict["name"]) # Если ключа нет - ошибка
print(my_dict.get("name")) # если ключа нет - None

# удаление элемента по ключу
print(my_dict.pop("name"))
print(my_dict)

# добавление элемента по ключу
my_dict["surname"] = "Ivanov"