from ch08.inheri1 import Derived, Base

class A(Derived):
    def m3(self):
        print("점심시간 멀었냐")

a = A()
a.m1(); a.m2(); a.m3()


