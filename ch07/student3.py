from time import ctime # 현재 시간 함수

class Student:
    schoolName = "한국"
    def __init__(self, name = "noname"):
        print("{}에 생성 되었습니다.".format(ctime()))
        self.name = name
    def __del__(self): # 객체 제거 될때
        print("{}에 객체가 삭제되었습니다. ".format(ctime()))
        
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

st1 = Student("효리"); st2 = Student(); st2.setName('상수')

# 객체 메모리에서 삭제
del st1; del st2

# print(("이름 : {}".format(st1.getName())))


