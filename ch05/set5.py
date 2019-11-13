a1 = {"해리","다혜", '하니','승기','다니엘'}
a2 = {'하니','승기','보희','철수'}
#합집합
print(a1.union(a2))
#교집합
print(a1.intersection(a2))
#차집합
print(a1.difference(a2))
#공통 제외하고 출력
print(a1.symmetric_difference(a2))
#효리가 a1에 포함되어 있는지 확인
if '효리' in a1:
    print('있다')
else:
    print('없다')