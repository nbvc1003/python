
# type 클래스는 클래스 유형을 만드는 용도
#
class Singleton(type):
    __instances = {}  # private 변수 (딕셔너리형 변수)

    def __call__(self, *args, **kwargs):
        if self not in self.__instances:
            self.__instances[self] = super().__call__() # type class의 매소드를 콜
        return self.__instances[self]


class A(metaclass=Singleton):
    pass
class C(Singleton):
    pass

a1 = A()
a2 = A()
# id() 메모리상의 주소 리턴
print(id(a1))
print(id(a2))

c1 = C()
# print(id(c1))