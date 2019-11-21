class A:
    def prn(self):
        print("대박")
class B1(A):
    def prn(self):
        print("허걱")

class C1(A):
    def prn(self):
        print("애휴")

# 모순된 경우 먼저 상속 받은 쪽에 우선권
class A2(B1, C1):
    # def prn(self):
    #     super().prn()
    pass
a2 = A2()
a2.prn()