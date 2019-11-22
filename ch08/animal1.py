
# Animal eat, abstractmethod move,
# Bird, Fish, Person
from abc import *

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def move(self):
        pass
class Bird(Animal):
    def eat(self):
        print("쪼아먹는다.")
    def move(self):
        print("날아다닌다.")
class Fish(Animal):
    def eat(self):
        print("물속에서 먹이를 먹는다.")
    def move(self):
        print("헤엄친다. ")
class Person(Animal):
    def eat(self):
        print("음식을 먹는다. ")
    def move(self):
        print("걸어다닌다")
    def speak(self):
        print("말한다.")

animals = [Bird(), Fish(), Person()]


for a in animals:
    a.eat()
    a.move()
    if isinstance(a, Person):
        a.speak()




