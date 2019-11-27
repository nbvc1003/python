import re
p = re.compile("(blue|white|red)")
# p = re.compile("blue|white|red")

# sub -> 문자를 바꾼다.
m = p.sub('color','blue socks and red shoes and white hat')
print(m)

# subn -> 변경과 변경된 갯수
m = p.subn('color','blue socks and red shoes and white hat')
print(m)