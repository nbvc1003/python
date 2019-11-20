

class Cat:
    #클래스 변수의 경우 static 변수처럼 사용가능
    name = "팽수"
    def __init__(self, age):
        self.age = age
    @classmethod
    def drink(cls):
        print("{}이 물을 먹는다. ".format(cls.name))
    @staticmethod
    def play():
        # 클래스변수 사용 방법 (static 변수와 성격이 유사)
        print("{}가 수다 떨고 있다".format(Cat.name))
    @staticmethod
    def play1(name):
        Cat.name = name
        print("{}가 수다 떨고 있다".format(Cat.name))
    def song(self):
        print("{}가 노래 부른다.".format(Cat.name))
        print("나이 :{}".format(self.age))


