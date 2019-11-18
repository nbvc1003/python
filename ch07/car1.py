
class Car: # 클래스명 은 대문자로시작
    def __init__(self): # 전역변수 선언 할때 사용 ( 생성자와 같다. )
        # 변수 선언및 변수 초기화.
        self.color = "red" # 클래스 전역으로 선언
        self.size = 18
        self.displacement = 2000
    test = 1.0
    #매소드, 함수 정의
    def forward(self):
        print("전진")
    def backward(self):
        print("후진")
    def turn_left(self):
        print("좌회전")
    def turn_right(self):
        print("우회전")

# main 프로세스에서 콜 했을경우만 아래 내용을 실행한다.
if __name__ == "__main__":
    # mycar 객체이름, reference 이름, instance
    mycar = Car() # Car클래스를 사용하여 mycar생성
    print(mycar.color)  # 객체명.속정
    mycar.backward()
    print(mycar.test)
        
    