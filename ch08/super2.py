# __init__ name, age를 받아서 self에 저장
# A __init__ 를 출력
# B에서 A를 상속받고 B __init__ 를 출력
# A의 생성자에 미호, 22살 입력하여 생성
# 이름과 나이를 출력하는 paint 매소드
# B의 객체 b1을 생성 , print 실행

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__('미호', 22)
    def print(self):
        print("이름 :{}, 나이 {}".format(self.name, self.age))


b1 = B()
b1.print()


