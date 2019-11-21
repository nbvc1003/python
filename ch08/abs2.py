from abc import *

class A (metaclass=ABCMeta):
    def prn(self):
        print("대박")
    @abstractmethod
    def p2(self):
        pass

class A1(A):
    def aa(self):
        print("사건 ")
    def p2(self):
        print("추상매소드 제정의")


a1 = A1()
a1.aa()