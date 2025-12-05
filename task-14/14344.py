from string import printable
for p in range(16, 37):
        num1 = int(f'17496', p)
        num2 = int(f'91F83', p)
        num3 = int(f'D9543', p)
        res = num1 + num2 + num3
        if res % 12 == 0:
            print(res // 12, p)