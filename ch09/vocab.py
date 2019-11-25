f1 = open('vocablory.txt', 'w', encoding='utf-8')
while True:
    print('영어단어')
    eng = input()
    if eng == 'q': break
    print('한글단어')
    kor = input()
    f1.write('{}:{}\n'.format(eng, kor))
print('단어장 완성')

f1.close()


