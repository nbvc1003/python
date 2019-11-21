class MyDeco:
    def __init__(self, func):
        print('초기화 작업')
        self.func = func
    def __call__(self, *args, **kwargs):
        print("함수 이름 : {}".format(self.func.__name__))
        self.func()
        for k in kwargs:
            print(k, kwargs[k])
        print("함수 종료")

# 데코레이션 사용밥법 1
# def hello():
#     print("안녕")
# hello = MyDeco(hello)
# hello()

# 데코레이션 사용밥법 2
@MyDeco
def hello():
    print("안녕")
hello()


hello(name = "린다", age = 23)

