import re

#함수로 공식을 만들고 해당 함수를 sub에서 적용

def hexaReplace(match):
    value = int(match.group())
    return hex(value) # 16진수로


p = re.compile(r'\d+') # 숫자만
m = p.sub(hexaReplace, 'Call 110 fro printing 15 for your code')
print(m)





