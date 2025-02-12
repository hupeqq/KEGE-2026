num = int(input())
mult = 1
while num:
    if num % 10 != 0:
        mult *= num % 10
    num //= 10
print(mult)