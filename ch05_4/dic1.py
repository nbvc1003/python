d1 = {'이름':'수지','나이':25,'취미':'욕하기','나이':12}
print(d1)
print(d1['나이']) # 같은 key값이 중복되면 앞 의값 무시
print(d1['이름'])

print(len(d1))
# 수정
d1['이름'] = '다혜'
print(d1['이름'])

del d1['나이'] # key에 해당하는 데이터 삭제
print(d1)