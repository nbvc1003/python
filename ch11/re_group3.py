import re

p1 = re.compile(r'\w+\s+\d+[-]\d+[-]\d+') # 문자/숫자
m = p1.match("park 010-1234-1234")
print(m)
print(m.group())


p2 = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)') # 문자/숫자
m = p2.match("park 010-1234-1234")
print(m)
print(m.group(0)) # 전체
print(m.group(1)) # 첫번째
print(m.group(2)) # 두번째 
print(m.group(3)) # 두번째 괄호 안의 세번째


# 그룹의 순서를 바꾸고 싶을경우
print(m.group(2) + ' ' + m.group(1))


