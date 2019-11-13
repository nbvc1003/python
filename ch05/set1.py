
hashset = set()   # set 데이터타입 생성 데이터 없는경우
print(hashset)

hashset = {1,2,3} # 데이터가 있을 경우 는 {}로 생성
print(hashset)

# tuple로 부터 생성 방법
hashset = set((1,2,3, 2)) # 중복된 2는 하나만 인자로 인식됨
print(hashset)

hashset = set('hello world') # 중복된 데이터 제거후 임의의 순서로 출력
print(hashset)

# list로 부터 생성 
hashset = set([1,6,7,6,1])
print(hashset)
