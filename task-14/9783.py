from string import printable
for x in printable[:22]:
    num1 = int(f'18{x}89957', 22)
    num2 = int(f'80{x}33', 22)
    num3 = int(f'521{x}6', 22)
    res = num1 + num2 + num3
    if res % 21 == 0:
        print(res // 21)