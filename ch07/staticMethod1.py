class Student:
    @classmethod
    def class_method(cls): # cls 가 반드시 들어간다.
        # 자신속한 클래스의 정보를 인자로 갖고 있다.
        print("클래스매소드 ")
        print(cls)

    @staticmethod
    def static_method(): # self 가 없다.
        print("정적매소드")
        
    def normal_method(self):
        print("일반매소드")

Student.class_method()
Student.static_method()

st1 = Student()
st1.normal_method()
st1.static_method()
st1.class_method()