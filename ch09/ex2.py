

f1 = open('test.txt', 'a', encoding='utf-8')

while True:
    print('저장할 내용을 입력하시요')
    msg = input()
    if msg == 'q': break
    f1.write(msg + '\n')

f1.close()
