from string import printable
for x in printable[:13]:
    num1 = int(f'9{x}AB', 13)
    num2 = int(f'{x}46C', 16)
    num3 = int(f'B7{x}', 15)
    res = num1 + num2 - num3
    if res % 14 == 0:
        print(res // 14, x)