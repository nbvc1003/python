
class A:
    def m3(self):
        print("난 A")


class C:
    def m3(self):
        print("난C")
class B:
    def m2(self):
        print("난 B")
# 다중상속의 경우 먼저 상속된 클래스의 매소드가 우선순위에 있다
# 아마도 관련 처리 절차가 Stack 에서 처리 되기 때문으로 추측된다.
class F(C,B,A):
    pass


f1 = F()

f1.m3(); f1.m2()


