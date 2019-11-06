# 4,5,8,2를 가진 list 생성
list = [4,5,8,2]
# 뒤에 11추가
list.append(11)
# 1번째 인덱스에 17추가
list.insert(1, 17)
# 5삭제
list.remove(5)
# 3번째 인덱스에 1 로변경
list[3] = 1
# 데이터를 거꾸로 출력
list.reverse(); print(list)
# 데이터를 정렬하고 출력
list.sort(); print(list)
# 17의 인덱스 값?
print(list.index(17))