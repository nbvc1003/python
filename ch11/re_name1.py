import re

p1 = re.compile(r'(\w+)\s+(\d+[-]\d+[-]+\d+)')
m = p1.search('park 010-1234-5678')
print(m.group(1))

# ?P<..> 그룹명 지정
p2 = re.compile(r'(?P<name>\w+)\s+((?P<kuk>\d+)[-]\d+[-]+\d+)') # 그룹에 이름을 지정
m = p2.search('park 010-1234-5678')
print(m.group("name"))
print(m.group("kuk"))

p3 = re.compile(r'(?P<name>\b\w+)\s+(?P=name)') # ?P=name -> name그룹을 한번 더쓸때

m = p3.search('Paris in the the spring')
print(m.group())