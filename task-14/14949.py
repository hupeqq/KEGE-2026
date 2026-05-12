from string import printable
for x in range(1, 8):
    num = int(f'{x}1{x}', 16) + int(f'{x}3{x}3', 8)
    if bin(num)[2:].count('1') == 1:
        print(num)