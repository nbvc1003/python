

from abc import *

class Car(metaclass=ABCMeta):
    @abstractmethod
    def drive(self): pass

class Ambulance(Car):
    def drive(self):
        print("환자를 싣고 달린다.")
    def move(self):
        print("사이렌을 울리며 달린다")
class Taxi(Car):
    def drive(self):
        print("총알처럼 달린다")
    def inwon(self):
        print("정원이 4명이다")
class Bus(Car):
    def drive(self):
        print("시내를 달린다")


ab = Ambulance(); tx = Taxi(); bus = Bus()
cars = [ab, tx, bus]

for car in cars:
    car.drive()
    if isinstance(car, Ambulance):
        car.move()
    elif isinstance(car, Taxi):
        car.inwon()


