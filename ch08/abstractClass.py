# 추상 클래스를 사용하기 위해 사전 ABCMeta 를 상속 받고
# 추상 메소드가 있어야 한다. 
from abc import ABCMeta, abstractmethod

class Abstract1(metaclass=ABCMeta):
    attr = "추상클래스 "
    # 추상매소드
    @abstractmethod
    def m1(self):
        pass
    #일반 매소드
    def m2(self):
        print("대박")

        