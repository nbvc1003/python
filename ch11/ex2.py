import re

p = re.compile('[a-z]+') # 영문자 소문자 여러개

#
m = p.search("5 python")

print(len("5 python"))
print(m.start(), m.end()) # m.end() == len()

# m.start() : 패턴에 맞는 첫번째 배열 인덱스
# m.end() : 패턴에 맞는 마지막 인덱스 (== len())
print(m.start() + m.end()) # 10 출력