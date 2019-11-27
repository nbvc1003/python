import re

# r 은 raw 첫글자는 _또는 영문자 두번째 글자부터는 특수문자 제외하고 전부 가능함
p = re.compile(r'[_a-zA-Z]\w*') # 첫글자가 _와 영문자만 허용하는 문자열

m = p.search('123 abc 123 def') # 조건에 맞는 첫단어 하나
print(m.group())

m = p.findall('123 abc 123 def') # 조건에 맞는 것 모두
print(m)


p = re.compile('the', re.I)  # re.I -> 대소문자 구별 안함
print(p.findall('The cat was hungry, They were scared because of the cat'))
