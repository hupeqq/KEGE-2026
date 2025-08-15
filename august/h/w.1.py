import re
with open("reg_exp_task_1.txt") as file:
    text1 = file.read()
    pattern1 = r'\d+'
    res = re.findall(pattern1, text1)
print(res)

import re
with open("reg_exp_task_2.txt") as file:
    text2 = file.read()
    pattern2 = r'-*\d*\.*\d+'
    res = re.findall(pattern2, text2)
print(res)

import re
with open("reg_exp_task_4.txt") as file:
    text3 = file.readline()
    pattern3 = r'\w+@\w+\.[a-z]{2,}'
    res = re.findall(pattern3, text3)
print(res)

pattern4 = r'[a]{1,}[b]{2,}[c]{1,}'
text4 = 'aaaabbbccccc'
res = re.sub(pattern4, "HELLO", text4, count=1)
print(res)
