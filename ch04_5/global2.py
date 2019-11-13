


def f1(a):
    global x # 전역변수로 지정
    x = a
    x = 7
    print('x =', x)

x=2
f1(x)
print('x=',x)