num = "9" * 136
while "22222" in num or '9999' in num:
    if "22222" in num:
        num = num.replace("22222", "99",1)
    else:
        num = num.replace("9999", '2',1)
print(num)