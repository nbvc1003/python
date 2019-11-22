
class Final(type):
    def __init__(self, name, bases, namespace):
        super().__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, Final):
                raise TypeError(klass.__name__ + ' is Final')

class A:
    pass

class B(A, metaclass=Final):
    pass

# class B(A, Final):
#     pass

class C(B):
    pass


