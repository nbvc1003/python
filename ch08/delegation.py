class A1:
    def __init__(self, li):
        self.li = li

    # 없는 매소드 실행시 불리는 매소드
    def __getattr__(self, item):
        for i in item:
            print("위임 : {}".format(i))
        # print("위임 {}".format(item), end = ' ')
        return getattr(self.li, item)

li = [1,3,5,6,3,9,1]
a1 = A1(li)
# getattr(li, 'pop')
# print(getattr(li, 'count({},{})'.format('self', 3)))
# print(li.count(3))


print(a1.pop())
print(a1.count(3))



