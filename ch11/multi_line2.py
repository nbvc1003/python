import re


# python 단어로 시작하고 공백, 숫자/문자 1자 이상
# re.M 여러개를 찾는다.
# p = re.compile('pt$', re.M) # 여러줄 각 각
p = re.compile('pt\Z',re.M) # 마지막줄만


data = """python one pt
life is too short pt
python two pt
you need pt"""
print(p.findall(data))

