import re

def change(match):
    print(match)
    return match.group() + "바보"


p = re.compile(r'\w+ !')
print('이름을 입력하세요')
name = input()
# m = p.sub(change, '당신은'+name)
m = p.sub(change, '당신은 {} !입니다.'.format(name))

print(m)

