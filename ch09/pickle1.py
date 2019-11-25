from ch09.dto import Person
import pickle

# 데이터의 직렬화와 저장 방법
# 원격으로 보낼때도 사용

p1 = Person(); p2 = Person()
p1.setNum(1);p1.setName('철수')
p2.setNum(2);p2.setName('영희')
li = [p1, p2]

# pickle 은 바이너리 파일로 데이터 저장할때 사용
with open('test.txt', 'wb') as f:
    pickle.dump(li, f)

with open('test.txt', 'rb') as f:
    # load 객체로 된 byte 데이터 읽을때
    result = pickle.load(f)
    for line in result:
        print(line.toString())
