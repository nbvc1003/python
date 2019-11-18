# Person class 생성
# 이름: 유미, 나이:25 , 성격:괘팍,
# act_hobby : 침을 뱃는다. , 졸고 있다. 
# 객체 p1 생성 이름 , 성격출력 act_hobby 실행
# 객체 p2 생성 : 이름 : 수미 변경, p1/p2 이름 출력

class Person:
    def __init__(self):
        self.name = "유미"
        self.age = 25
        self.character = "괘팍"
    def act_hobby(self):
        print("졸고있다. ")


p1 = Person()
print(p1.name)
p1.act_hobby()

p2 = Person()
p2.name = "수미"

print(p1.name)
print(p2.name)



