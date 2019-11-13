s1 = {3,5,7}
s1.add(6)

s2 = s1.copy() # 주소가 아닌 데이터 자체를 복사한다.
s1.add(9)

print(s1)
print(s2)

s1.discard(5) # 없어도 상관없다.
s1.remove(7) # 반드시 있는 값만..

print(s1)
s1.discard(10) # 없는 숫자를 discard 하면 그냥 통과
#s1.remove(10) # 없는 숫자를 remove할경우 애러발생

# pop 데이터를 앞에서부터 하나씩 추출하여 제거
while s2:
    print(s2.pop())