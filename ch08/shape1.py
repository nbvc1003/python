# Shape print() 모형을 출력한다.
# Triangle , Circle, Rectangle 에 각각 prn()
# 삼각형 , 원, 사각형을 출력한다.
# for 문을 사용하여 삼각형 , 원, 사각형 을 출력한다는 문장

class Shape:
    def prn(self):
        print("모형을 출력 한다. ")

class Triangle(Shape):
    def prn(self):
        print("삼각형을 출력한다. ")
class Circle(Shape):
    def prn(self):
        print("원을 출력한다. ")
class Rectangle(Shape):
    def prn(self):
        print("사각형을 출력한다. ")


shapes = [Triangle(), Circle(), Rectangle()]
for s in shapes:
    s.prn()