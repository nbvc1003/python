

data = ['Morning','Afternoon','evening','Night']
data.sort()
print(data)

# 정렬하는 동한은 전부 소문자로 변경하여 처리
data.sort(key = str.lower)
print(data)