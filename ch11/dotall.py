import re


p = re.compile('a.b') #  \n 제외한 문자
m = p.match('a\nb')
print(m)
m = p.match('akb')
print(m)
m = p.match('a.b')
print(m)
print("--------------------------------------------------------------")

p = re.compile('a.b', re.DOTALL) # \n도 매치하도록 함
m = p.match('a\nb')
print(m)
m = p.match('akb')
print(m)