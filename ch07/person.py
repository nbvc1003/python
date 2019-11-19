

# Person class name, age, addr 속성
# __init__ 통해서 셋팅하고 각각을 출력하는 프로그램 작성

class Person:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    def print(self):
        print(self.name, self.age,self.addr)


p1 = Person("하니",21, "마포")
p2 = Person("미호",22, "신촌")
p3 = Person("다니엘",23, "강남")
p1.print();p2.print();p3.print()
Person.print(p3)

print(p1.__str__())
