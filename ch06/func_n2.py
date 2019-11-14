
def plus(x,y):
    print(x + y)

def minus(x,y):
    print(x - y)


plus(2, 3)
minus(3, 2)

# 함수를 리스트의 원소처럼 쓸수 있다.
f = [plus, minus]

f[0](2,4)
f[1](4,2)




