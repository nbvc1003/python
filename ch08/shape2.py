from abc import *

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass
class Triangle(Shape):
    def draw(self):
        print("삼각형을 그려라")


class Rectangle(Shape):
    def draw(self):
        print("사각형을 그려라 ")
class Circle(Shape):
    def draw(self):
        print("원을 그려라 ")

shapes = [Triangle(), Rectangle(), Circle()]

for ins in shapes:
    ins.draw()


