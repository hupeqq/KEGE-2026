num = str(10**90)
while "1" in num:
    if "10" in num:
        num = num.replace("10", "0001",1)
    else:
        num = num.replace("1", '000',1)
cnt = num.count('0')
print(cnt)

