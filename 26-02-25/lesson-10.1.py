# Строки в Python представляют собой не изменяемую последовательность символов.
# Последовательность — это коллекция, в которой каждый элемент имеет свой индекс
# и элементы могут быть не уникальными.

# Работа с индексами. Срезы
#
# s[n:m:k]
# Где s - имя переменной строкового типа, n, m, k выражения целого типа (k≠0).
# n - начало среза
# m - конец среза (НЕ ВКЛЮЧИТЕЛЬНО)
# k - шаг среза
# Если внутри квадратных скобок стоит одно двоеточие, то считается,
# что это двоеточие между первым и вторым параметрами (n и m).
# В этом случае мы получим последовательность от n -го символа до m−1 -го
# Если не указан первый параметр (начало подстроки),
# то его значение полагается равным 0
# Если не указан второй параметр (конец подстроки),
# то он полагается равным всей длине последовательности
# Если не указан третий параметр (шаг), то он полагается равным 1.
text = 'Hello World!'
print(text[:5])