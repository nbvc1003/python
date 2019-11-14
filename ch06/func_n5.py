def anyoung():
    print('안녕하세요')

def hell():
    print('hello')

def greet(f):
    if f == 'k':
        result = anyoung
    else:
        result = hell
    return result

x = greet('k')
x() # () 함수를 실행..
x = greet('e')
x()

