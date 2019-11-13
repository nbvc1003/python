
a = 3

def outer():
    a = 7
    def inner():
        nonlocal a # a를 현재 함수 바로 밖의 a로 지정.
        #global a # a를 전역 a로 지정 같다.
        print('inner a=',a)
        a = 10
    inner()
    print('inner실행 a=', a)

outer()
print('외부 a=',a)
