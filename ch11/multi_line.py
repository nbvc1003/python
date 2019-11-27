import re


# python 단어로 시작하고 공백, 숫자/문자 1자 이상
# re.M 여러개를 찾는다.
p = re.compile('^python\s\w+', re.M)

data = """python one life is too short
python two
you need python 
python three
"""

print(p.findall(data))