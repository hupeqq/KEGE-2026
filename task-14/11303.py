from string import printable
for x in printable[:20]:
    num1 = int(f'627{x}J8', 20)
    num2 = int(f'H45I{x}5HIJ', 20)
    num3 = int(f'4IDB49J{x}7', 20)
    res = num1 + num2 + num3
    if res % 19 == 0:
        print(res // 19)