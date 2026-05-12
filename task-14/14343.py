num = 5*343**2031 + 4*49**2142 - 3*7**111 + 7**222
cnt = 0
while num:
    cnt += num % 7
    num //= 7
print(cnt)