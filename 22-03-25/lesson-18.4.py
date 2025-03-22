for n in range(4, 10000):
    num = "1" + "2" * n
    while "12" in num or '322' in num or "222":
        if "12" in num:
            num = num.replace("12", "2")
        if "322" in num:
            num = num.replace("322", "21")
        if "222" in num:
            num = num.replace("222", "3")
    cnt = 0
    for i in num:
        cnt += int(i)
    if cnt == 15:
        print(n)



