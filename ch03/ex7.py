

# names = ['호동','재석','포동','희철','효리']
names = ['호동','재석','포동','희철','효리']
# 인덱스 1번째에 '하니' 추가
names.insert(1, '하니')
# 인덱스 3번째에 ['아이유', '제니'] 추가
names[3:2] = ['아이유','효리']
# index 0번째 데이터 삭제
names.remove('호동') # 값으로 삭제
del names[0] # 인덱스로 삭제
# 인덱스 를 이용하여 처음부터 끝까지 출력
print("-------------------------------------")
for i in range(len(names)):
    print(names[i])
# 데이터를 직접가져와 처음부터 끝까지 출력
print("-------------------------------------")
for i in names:
    print(i)
# pop을 이용하여 뒤부터 출력
print("-------------------------------------")
while names:
    print(names.pop())