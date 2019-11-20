
class Student:
    def __init__(self, name = "몰라"):
        self.name = name
    def set_name(self,name):
        print("setter name 호출")
        self.__name = name  # private 변수 명명법
    def get_name(self):
        print("getter 호출")
        return self.__name
    def set_age(self, age):
        if age < 0 :
            print("나이는 양수야")
            self.__age = 0
        else:
            print("setter age 호출")
            self.__age = age
    def get_age(self):
        print("getter age 호출")
        return self.__age
    
    # 변수의 getter, setter 매소드를 지정해준다.
    # 변수의 private 지정 대안 으로 사용가능
    # 변수의 접근 제한 or 조회 제한 가능
    age = property(get_age, set_age) # 순서는 getter, setter
    name = property(fset=set_name, fget=get_name) # 명시적으로 지정


st1 = Student('수미')
print(st1.name)
st1.name = '유미'
print(st1.name)

st1.age = -5
