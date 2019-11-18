class User:
    pass

# python에서 맴버변수를 외부에서 추가 할수 있다...
# 대신 다른 객체에서는 사용못한다.
u1 = User()
u1.name = "혜리"
u1.age = 22
u1.hobby = "잔소리"

print(u1.name, u1.age, u1.hobby)

u2 = User()
u2.name = "강다니엘"
u2.hobby = "영화보기"

print(u2.name,  u2.hobby)

# User 클래스가 다시 정의 된다.
class User:
    def __init__(self):
        self.name =""
        self.age =0
        self.hobby = ""

u2 = User()
print(u2.age)