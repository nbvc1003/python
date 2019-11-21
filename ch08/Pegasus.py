class Bird:
    def move(self):
        print("날개로 난다.")

class Horse:
    def move(self):
        print("네발로 달린다")

class Pegasus(Bird, Horse):
    def move(self):
        print("지상에서는 달리고  하늘에서는 난다")

p1 = Pegasus()
p1.move()