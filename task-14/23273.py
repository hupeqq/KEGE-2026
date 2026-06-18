from string import printable

for x in printable[:29]:
    num = int(f'463{x}7921', 29) + int(f'8241{x}153', 29)
    if num % 28 == 0:
        print(num // 28)