for x in range(0, 18):
    num1 = int(f'78{x}79643', 19)
    num2 = int(f'25{x}43', 19)
    num3 = int(f'63{x}5', 19)
    res = num1 + num2 + num3
    if res % 18 == 0:
        print(res // 18)