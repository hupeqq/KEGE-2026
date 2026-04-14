# системы счисления
n = 25
# двоичная система
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
print(bin(n)[2:])
# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
print(f'{n:b}')
# восьмеричная система
print(oct(n)[2:])
print(f'{n:o}')
# шестнадцатеричная система
print(hex(n)[2:])
print(f'{n:x}')
# перевод в любую систему (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
# перевод в любую систему (2 <= sys <= 36)
from string import printable
def convert2(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
# перевод в десятичную
num_bin = '101'
num_tri = '201'
num_hex = 'f01'
print(int(num_bin, 2))
print(int(num_tri, 3))
print(int(num_hex, 16))
# срезы
# взятие двух первых цифр
data = '7777'
print(data[:2])
# взятие без двух первых цифр
print(data[2:])
# взятие двух последних цифр
print(data[-2:])
# взятие без двух последних цифр
print(data[:-2])
# сумма цифр числа
# двоичная система
num1 = '1010'
sum1 = num1.count('1')
# любая система до 10 вкл
num2 = '1210'
sum2 = sum(map(int, num2))
# люба система до 36 вкл
num3 ='AF5'
sum3 = sum(map(lambda x: int(x, 36), num3))
print(sum3)


