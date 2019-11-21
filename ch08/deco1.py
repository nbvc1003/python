class Call:
    # 객체 이름으로 실행 할경우 자동 실행되는 매소드 .
    def __call__(self, *a):
        print("대박이야.", a)
c1 = Call()

c1()
c1('뭐지')

c1('뭐지','허걱','허각','허공')