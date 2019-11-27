import re

# 옵션없을 경우 대소문자 구분해서 매치
p = re.compile('[a-z]')
m = p.match('python')
print(m)
m = p.match("Python")
print(m)
m = p.match('PYTHON')
print(m)

print('--------------------------------------------')

# re.I 경우 대소문자 구분없이 매치
p = re.compile('[a-z]', re.I)
m = p.match('python')
print(m)
m = p.match("Python")
print(m)
m = p.match('PYTHON')
print(m)