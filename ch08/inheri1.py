
class Base:
    def m1(self):
        print("대박")

class Derived(Base): # python에서 상속 방법
    def m2(self):
        print("사건")



if __name__ == "__main__":
    b1 = Base()
    b1.m1()
    d1 = Derived(); d1.m1(); d1.m2()