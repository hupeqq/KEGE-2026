for x in range(1, 150):
    num1 = 5*150**4 + 1*150**3 + x*150**2 + 2*150 + 9
    num2 = x*150**3 + 0*150**2 + 2*150 + 3
    res = num1 + num2
    if res % 149 == 0:
        print(res // 149)