class Student:
    # 클래스 변수 ( 변수)
    schoolName = "한국"
    def __init__(self, addr):
        self.addr = addr

st1 = Student("신촌"); st2 = Student("마포")
#클래스 변수는 객체명.변수명 or 클래스명.변수명
#인스턴스 변수는 불가
print("학교명 : {}".format(st1.schoolName))
print("학교명 : {}".format(Student.schoolName))
print("주소 :{}".format(st1.addr))

# 인스턴스 변수와 클래스 변수는 아래와 같이 사용 가능
print("주소 : {}".format(st1.addr))
# 인스턴스 변수의 경우 클래스에서 바로 접근해서 사용할수 없다.
# print("주소 : {}".format(Student.addr))

Student.schoolName = "코리아"; st1.addr = "강남"
print("학교명 : {}".format(st2.schoolName))
print("학교명 : {}".format(Student.schoolName))
print("주소 :{}".format(st2.addr))


# 각자 다른 변수 ? static 변수가 아닌듯..
Student.schoolName = "코리아"
st1.schoolName = "222"
st2.schoolName = "333"
