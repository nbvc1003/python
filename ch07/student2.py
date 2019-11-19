class Student:
    schoolName = "한국"
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self,age):
        if age < 0:
            print("나이는 0보다 작을수 없습니다. ")
        else:
            self.age = age
    def getAge(self):
        return self.age

st1 = Student()
st1.name = "철수"
print("이름 :{}".format(st1.name))
st1.setName("팽수")
print("이름 : {}".format(st1.getName()))

st1.age = -10
print("나이 : {}".format(st1.getAge()))
st1.setAge(-10)