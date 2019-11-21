class Delegate:
    def __init__(self, st):
        self.st = st
    def __getattr__(self, item):
        # print(type(item))
        print("위임 : {}".format(item), end=" ")
        return getattr(self.st, item)
    def prn(self):
        return "대박사건"
    def speak(self):
        print("배고파")

st = "Good Morning BMy Friend"

# del 객체
# 객체 . count ('nn)

d1 = Delegate(st)


# 아래 두가지 코드는 동일하다.
print(getattr(st, 'count')('n'))
print(d1.count('n'))
# 추가 설명
# getattr(st, 'count') -> st 라는 list에 count 라는 매소드의 포인트를 리턴한다.
# 따라서 뒤에 (인자. ) 이런식으로 매소드처럼 사용가능 하다.
# 실제 def __getattr__(self, item): 함수에서 item 이외에 인자 값들은 확인할 수 없는 이유이기도 하다.




