
x = 0
def f1():
    x = 7
    print('x =',x)

f1()
print('x = ',x)

#출력했을때 어떤 값이 ?
#밖과 안이 같은 값으로 출력하게 변경
def f1():
    global x
    x = 7
    print('x=',x)

f1()
print('x = ',x)


# f2(2,5,8,3,5) 2와 나머지 데이터 출력 하는 함수 작성
def f2(a, *b):
    print(a)
    print(b)

f2(2,5,8,3,5)

# f3(name='보미', age=21, hobby='지각', food='빵')
# 이름, 나이, 나머지 출력 하는 함수
def f3(name, age, **etc):
    print('이름 :', name)
    print('나이 :', age)
    print(etc)

f3(name='보미',age=21, hobby='지각', food='빵')
