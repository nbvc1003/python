import re


# python 단어로 시작하고 공백, 숫자/문자 1자 이상
# re.M 여러개를 찾는다.
# p = re.compile('^python\s\w+', re.M) # 여러줄 각각이 python으로 시작
p = re.compile('\Apython\s\w+', re.M) # 첫번째 줄의 python시작만 

data = """python one 
life is too short
python two
you need python 
python three
"""

print(p.findall(data))