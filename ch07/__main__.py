

# __main__ 이름의 파일은 주로 실행 전문 코드를 담는 파일
# 클래스나 매소드 보다는 스크립트 위주로 작성한다.
# 다른 언어의 main() 의 역활을 한다.

from ch07.student1 import Student


st1 = Student()
st2 = Student()
st1.start()
st1.printName("팽수")
Student.start(st2)
Student.printName(st2, '유산슬')


