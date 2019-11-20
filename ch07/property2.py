# property name, age  : age는 음수는 에러 , get, set 을 반드시 사용
# p1 객체를 생성하고 이름과 나이를 변경하여 출력

class Person:
    def __init__(self, name):
        self.__name = name
    def set_age(self, age):
        if age < 0:
            print("음수입니다. ")
            self.__age = 0
        else:
            self.__age = age
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def del_test(self): # ? 해당케이스를 찾지 못했다.
        print("del tset")

    age = property(get_age, set_age, fdel=del_test)
    name = property(get_name, set_name)

p1 = Person("철수")

p1.age = 5
p1.name = "영희"
print("{}의 나이는 {}".format(p1.name, p1.age))

Person.name = "광수"
Person.age = 10
print(p1.name)
p2 = Person("jc")

print(p2.age)


