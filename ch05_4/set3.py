a1 = {1,2,3,4,5}
a2 = {4,5,6,7,8}
a3 = {9,10,11,12}

#union 합집합 : 공통 부분을 한번만 추출
print(a1.union(a2))
#intersection 공통집합, 교집합
print(a1.intersection(a2))
#difference 는 차집합
print(a1.difference(a2))
#공통되지 않은 부분만 출력
print(a1.symmetric_difference(a2))

# 교집합이 없으면 True
print(a1.isdisjoint(a2))
print(a1.isdisjoint(a3))
