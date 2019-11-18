class User:
    def introduce(someone):
        print(someone.name, someone.age)

u1 = User(); u2 = User()
u1.name = "하니"; u1.age = 12
u2.name = "다니엘"; u2.age =22


# 매소드를 사용하는 방법 2가지 
User.introduce(u1)
User.introduce(u2)

u1.introduce()
u2.introduce()