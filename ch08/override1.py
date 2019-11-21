class A1:
    def m1(self):
        print('난 A야 ')

class A2(A1):
    def m1(self):
        print("난 A2야")

class A3(A2):
    def m1(self):
        print("난 A3야")


a1 = A1()
a2 = A2()
a3 = A3()
a1.m1()
a2.m1()
a3.m1()