import sys
sys.set_int_max_str_digits(500000)
num = 15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809
cnt_0 = 0
cnt_1 = 0
while num:
    if str(num % 7) in '0246':
        cnt_1 += 1
    else:
        cnt_1 += 1
    num //= 7
print(abs(cnt_0 - cnt_1))