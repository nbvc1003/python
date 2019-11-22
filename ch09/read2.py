

text = open('test.txt', 'r', encoding='utf-8')
for line in text:
    print(line, end="")

text1 = open('test.txt', 'r', encoding='utf-8')
content = text1.read()
print(content)

text2 = open('test.txt', 'r', encoding='utf-8')
textList = text2.readlines()
print(textList)

text.close()
text1.close()
text2.close()
