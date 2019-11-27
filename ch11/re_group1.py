import re

p = re.compile('(ABC)+')
# ( ... ) 이런식으로 괄호가 쓰이면 괄호내 내용이 한묶음으로 묶여 있다는 뜻

m = p.match('ABCABCKKABCAABB OK')
print(m)
print(m.group())