import re

# r ?
p1 = re.compile(r'\bclass\b') # class 문자의 앞뒤 공란 까지 포함해서 있어야
# \b : 공란이 있어야 한다 , \B : 공란이 없어야 한다
p2 = re.compile(r'class') # class 문자열 포함여부만

print(p1.search('no class at all'))
print(p2.search('no class at all'))
print(p1.search('the declassifed algorithm'))
print(p2.search('the declassifed algorithm'))

