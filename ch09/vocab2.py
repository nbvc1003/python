f = open('vocablory.txt', 'r', encoding='utf-8')

# open 은 옵션에 따라서 리턴 형식이 여러가지가 있다.

for line in f:
     li = line.split(':')
     print('{}의 뜻? '.format(li[0]))
     inE = input()
     if inE.strip() == li[1].strip():
        print('정답입니다.')
     else:
        print('오답니다. 정답은{}'.format(li[1]))

f.close()