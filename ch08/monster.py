class Person:
    def move(self):
        print("두발로 걷는다.")

class Bird:
    def move(self):
        print("날개로 난다")

class Fish:
    def move(self):
        print("헤엄친다.")

class Monster(Person, Bird, Fish):
    def move(self):
        print("지상에서는 걷고 하늘에서 날고 물에서헤엄")

m1 = Monster()
m1.move()