

# startwidth 시작확인

a1 = "Hello"
print(a1.startswith("H"))
print(a1.startswith("F"))
print(a1.endswith("o"))
print(a1.endswith("d"))

# count 는 해당 문자의 갯수

print(a1.count('l'))


# strip 공백제거

s1 = "                     대 박"
print(s1.lstrip()) # d왼쪽 공란제거
print(s1.rstrip()) # 오른쪽 공란 제거
print(s1.strip()) # 좌우 공란 제거



