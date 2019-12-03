

class Student:
    def __init__(self):
        self.__name = '무명'

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name
    name = property(getName,setName)

st = Student()
st.name = "test"
print(st.name)


