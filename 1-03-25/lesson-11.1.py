text = "Hello"
search_substr = "1"
#print(text.index(search_substr))
len_search_letter = len(search_substr)
for i in range(len(text) - len_search_letter + 1):
    if text[i:i + len_search_letter] == search_substr:
        print(i)
        break
else:
    print("Такой подстроки в строке нет")

poz = 0
while text:
    if text[:len(search_substr)] == search_substr:
        print(poz)
        break
    poz += 1
    text = text[1:]

else:
    print("Такой подстроки в строке нет")