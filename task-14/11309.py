from string import printable
for x in printable[:27]:
    num1 = int(f'8{x}38{x}68', 27)
    num2 = int(f'37{x}3163', 27)
    res = num1 + num2
    if res % 26 == 0:
        print(res // 26)