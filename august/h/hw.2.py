import re
with open("regexp-practice-7.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'[a-zA-Z0-9-.]+@[a-zA-Z0-9-.]+\.[a-z]{2,}'
    res = re.findall(pattern, text)
print(res)

import re
with open("regexp-practice-9.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'(https://[a-zA-Z0-9-.]+\.[a-z]{2,}|http://[a-zA-Z0-9-.]+\.[a-z]{2,})'
    res = re.findall(pattern, text)
print(res)

import re
with open("regexp-practice-10.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'\d'
    res = re.sub(pattern, '#', text, count=1000000)
print(res)

import re
with open("regexp-practice-11.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'<.*>'
    res = re.sub(pattern, '', text, count=1000000)
print(res)
