# Person speak() 떠든다. move() 두다리로 걷는다.
# Fish move() 지느러미로 해엄친다.
# Muraid 위의 것을 상속 speak(), move()

class Person:
    def speak(self):
        print("떠든다")
    def move(self):
        print("두 다리로 걷는다")
class Fish:
    def move(self):
        print("지느러미로 해엄친다. ")

class Murmaid(Person, Fish):
    # def move(self):
    #     super().
    pass



m1 = Murmaid()
m1.speak()
m1.move()