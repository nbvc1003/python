# Cat 초기 이름 샛팅
# setAge, getAge, 나이저장, 나이get
# print() 이름과 나이 출력매소드
# ntime() 숫자만큼 출력 반복하는 매소드

class Cat:
    def __init__(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def print(self):
        print("이름 :{}, 나이 {}".format(self.name, self.age))
    def ntime(self, n):
        for i in range(n):
            self.print()

c1 = Cat("나비")

c1.setAge(10)
c1.print()

c1.setAge(2)
c1.print()
c1.ntime(3)