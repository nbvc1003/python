

import re

p = re.compile(r'(\b\w+)\s+\1') # \1 -> group(1)이 반복
# \2 group(2) 가 반복

m = p.search('Paris in the the spring')
print(m.group())