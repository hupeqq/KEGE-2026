import re
with open("Regexp contest/regexp-practice-1.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'\b[cC][aA][tT]\b'
    res = re.findall(pattern, text)
print(res)

with open("Regexp contest/regexp-practice-2.txt", encoding='utf-8') as file:
    text = file.readlines()
    pattern = r'[aA]'
    for i in text:
        if re.match(pattern, i):
            print(i)

with open("Regexp contest/regexp-practice-3.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'(-?\d+)(\.\d+)?'
    res = re.findall(pattern, text)
print(res)

with open("Regexp contest/regexp-practice-4.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'\d{1,2}-\d{1,2}-\d{4}'
    res = re.findall(pattern, text)
print(res)

with open("Regexp contest/regexp-practice-5.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'[A-ZА-ЯЁ][a-zа-яё]*?\b'
    res = re.findall(pattern, text)
print(res)

with open("Regexp contest/regexp-practice-6.txt", encoding='utf-8') as file:
    text = file.read()
    pattern = r'[A-ZА-Яа-яa-z][A-ZА-Яа-яa-z]-\d{4}'
    res = re.findall(pattern, text)
print(res)





