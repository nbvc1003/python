

class Delegation:
    def __init__(self, li):
        self.li = li
    def __getattr__(self, item):

        print("Delegation {}".format(item))
        # getattr (a, b) : a데이터셋 안에 b값이 존재 하는지 1/0 True/False 로 리턴한다.
        print(self.li, item)
        print(self.li, item)
        # list = [1,2,3]
        # print(list.count(1))

        return getattr(self.li, item)
        # 해석 getattr([2,3,5,7,9,2,1], count(2))
        # getattr(a, b) 할수 : a 리스트의 , count(2)의 값을 리턴한다.
        # Delegattion클래스에 count함수가 없기때문에 __getattr__매소드로 등어온다. 
        # 그리고 인자로 그 없는 매소드 명을 가져온다. 
        # 내부에서 getattr(self.li, count(2)), == self.li.count(2) 실행

ob = Delegation([2,3,5,7,9,2,1])
print(ob.pop())
print(ob.count(2))

