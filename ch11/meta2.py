import re

# $는 끝나는 문자 short 으로 끝나는지

print(re.search("short$", "Life is too short, you need python"))

print(re.search("short$", "Life is too short"))

# '$' 글자를 찾을때는 []를 사용
print(re.search("[$]", "Life is too $ short"))
print(re.search("\$", "Life is too $ short")) # 위와 동일

