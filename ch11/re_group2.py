import re

p1 = re.compile(r'\w+\s+\d+[-]\d+[-]\d+') # 문자/숫자
m = p1.match("park 010-1234-1234")
print(m)
print(m.group())


p2 = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)') # 문자/숫자
m = p2.match("park 010-1234-1234")
print('이름 :', m.group(1))
print('전화 :', m.group(2))



