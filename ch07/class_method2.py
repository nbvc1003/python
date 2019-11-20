
# Cat name = 팽수 class 변수
# class method drink name 이 물을 먹는다.
# static play 수다떨고 있다.
# 일반 song 노래 부른다.
# 클래스 명으로 매소드 실행, 객체 c1 생성 실행

class Cat:
    #클래스 변수의 경우 static 변수처럼 사용가능
    name = "팽수"
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

Cat.drink()
Cat.play()
Cat.play1("냐옹")
c1 = Cat()
c1.song()
c1.drink()
c1.play1("나비")
Cat.play()
c2 = Cat()
Cat.name = "고양이"
c2.play()

# Cat.name , c1.name 동일한 변수

