f = open('add1.txt','a', encoding='utf=8')
f. write('대박')
f.close()

#  w 옵션 :  기존 데이터 를 지우고 새로 쓴다.
f = open('add1.txt','w', encoding='utf=8')
f. write('사건\n')
f.close()

#  a 옵션 :  기존 데이터 를 지우지 않고 추가한다.
f = open('add1.txt','a', encoding='utf=8')
f. write('지우지마')
f.close()