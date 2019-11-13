d1 = {'이름':'하니','나이':23,'취미':'노래'}
print(d1.keys(), type(d1.keys())) # 키값 리스트
print(d1.values()) # value값 리스트
print(d1.items()) # keyValue 값

d2 = d1.copy()
d1.clear()

print(d1)

# 해당 키값의 value를 출력
print(d2.get('이름'))
print(d2.get('나이',['대박']))
print(d2.get('고향',['대박'])) # 키가 있으면 value 없으면 '대박' 이 출력

