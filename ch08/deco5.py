
# c


class Deco2:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("초기매쏘드 네임 : {}".format(self.func.__name__))
        self.func()
        for k in kwargs:
            print(k)

## @Deco2
## 형식으로 사용할때 __init__ 생성자 함수에 인자로 함수 변수 필요

@Deco2
# Deco2 클래스의 prn 이라는 객체를 생성한다. 
def prn():
    print("안녕 컴동지등 ")

# 객체에 dictionary 데이터를 대입하여 객체를 실행
prn(name = "철수", age=43, hobby="졸기")


