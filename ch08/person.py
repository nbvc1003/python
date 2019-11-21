class Person:
    def __init__(self, name, age):
        self.name = name; self.age = age
    def prn(self):
        print("========================================")
        print("이름 : {}".format(self.name))
        print("나이 : {}".format(self.age))


class Student(Person):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby
    def prn(self):
        super().prn()
        print("취미 :{}".format(self.hobby))

class Teather(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    def prn(self):
        super().prn()
        print("과목 :{}".format(self.major))

class Staff(Person):
    def __init__(self, name, age, part):
        super().__init__(name, age)
        self.part = part
    def prn(self):
        super().prn()
        print("담당 :{}".format(self.part))


st1 = Student('제니', 23, '졸기')
st2 = Student('하니', 25, '놀기')

th1 = Teather('제석', 46, '파이썬')
th2 = Teather('명수', 50, '머신러닝')

s1 = Staff('스태프',22, '관리')

data = [st1, st2, th1, th2, s1]
for d in data:
    d.prn()



