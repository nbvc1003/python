

class A:
    test = "test"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def prn(self):
        print("prn A")
class AE:
    test = "testAB"
    def prn(self):
        print("prn AE")


class B(A, AE):
    def __init__(self):
        print("B.__init__")
        super().__init__('미호', 22)
    def print(self):
        print("이름 :{}, 나이 {}".format(self.name, self.age))
    def prn(self):
        super().prn()
        print("prn B")


b1 = B()
b1.print()
b1.prn()
print(b1.test)