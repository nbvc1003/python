

# frozoneset 은 생성된 값으로 고정됨 추가, 수정, 부분삭제 안됨
# 다른 성격은 set와 같다. 
a1 = frozenset()
# a1.add(7)
print(a1, type(a1))
a1 = frozenset((1,2,3))
print(a1)
a1 = frozenset([0,1,2,3,1])
print(a1)
a1 = frozenset(range(5))  # 0~5 값
print(a1)
print(len(a1))


