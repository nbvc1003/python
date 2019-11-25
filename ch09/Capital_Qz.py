f1 = open('capital.txt', 'r', encoding='utf-8')
for inn in f1:
    li = inn.split(':')
    cp = input('{}의 수도는 ?'.format(li[0]))
    if li[1].strip() == cp:
        print('정답')
    else:
        print('오답 정답은 {}'.format(li[1]))

f1.close()