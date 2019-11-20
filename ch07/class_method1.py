class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1 # 객체를생성하면 1증가
    @classmethod
    def print_cm(cls):
        print(cls.count)
    def print_nm(self): #일반 매소드는 클래스 변수 사용 못한다.
        print(Counter.count)

if __name__ == "__main__":
    Counter.print_cm()
    c0 = Counter()
    Counter.print_cm()
    c1 = Counter()
    #c1.count += 1
    c1.print_cm()
    #print(c1.count)
    Counter.print_cm()
