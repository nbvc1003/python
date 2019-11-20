# A m1() 점심시간
# B 는 A를 상속 받아서 m2() 1차 프로젝트 종료
# C 는 B를 상속 받아서 m3() 뭐 그러네
# C 에서 c1 객체 사용하여 m1, m2, m3 실행

class A:
    def m1(self):
        print("점심시간")

class B(A):
    def m2(self):
        print("1차프로젝트 종료")

class C(B):
    def m3(self):
        print("뭐그러네")

c1 = C()

c1.m1(); c1.m2();c1.m3()