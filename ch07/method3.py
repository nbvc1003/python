
class User:
    def introduce(someone, n):
        for i in range(n):
            print(someone.name, someone.age, someone.hobby)

# ui, u2, 이름, 나이, 취미
# u1은 클래스명.매소드(), u2.메소드(), n은 빈복횟수
# n을 u1일때 2회, u2일때 3회

u1 = User()
u1.name = "U!"
u1.age = 24
u1.hobby = "U1Hobby"

u2 = User()
u2.name = "U2"
u2.age = 26
u2.hobby = "U2Hobby"

#
User.introduce(u1, 2)
# 1번째 인자를 생략할경우 객체 자체를 인자로 가져 간다?
u2.introduce(3)

