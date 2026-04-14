text = input()
# служит для подсчета количества элементов последовательности
print(len(text))
cnt = 0
for i in text:
    cnt += 1
print(cnt)
cnt1 = 0
while text:
    cnt1 += 1
    text = text[:-1]
print(cnt1)