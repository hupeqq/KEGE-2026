from string import printable
for x in printable[:18]:
    num1 = int(f'11H{x}05', 18)
    num2 = int(f'3F{x}54{x}8', 18)
    num3 = int(f'G{x}{x}{x}9', 18)
    res = num1 + num2 + num3
    if res % 14 == 0:
        print(res // 14, x)