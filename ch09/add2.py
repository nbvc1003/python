
f = open('add2.txt','a', encoding='utf-8')
for i in range(1,10):
    f.write('{}개 추가 했습니다.\n'.format(i))

f.close()