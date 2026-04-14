str1 = input()
if str1.lower() == str1[::-1].lower():
    print('Слово-палиндром')
else:
    print("Слово - не палиндром")
