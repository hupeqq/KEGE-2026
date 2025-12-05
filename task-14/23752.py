from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num%sys]
        num //= sys
    return res[::-1]
num1 = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
num27 = convert(num1, 27)
cnt = 0
for i in num27:
    if i in printable[10:27]:
        cnt += 1
print(cnt)



