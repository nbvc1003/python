
#딕셔너리 데이터 타입 생성
a = dict()
print(a)

a['name'] = 'python'
print(a)

# 키에 tuple 형 가능
a[('a',)] = 'python'
print(a)

# key에 list 형이 올수 없다.
# a[[1]] = 'python'
# print(a)

a[1] = 'python'
print(a)

a[250] = 'python'
print(a)

# disct 형 데이터의 키에는 value 또는 변경 불가한 데이터 타입만 가능하다.
