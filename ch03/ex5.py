

#num = [9,7,8] 생성
num = [9,7,8]
# 9추가
num.append(9)
# [11,23]추가
num.extend([11,23])
# [1,5] 를 +로 추가
num = num + [1,5]
# 5의 갯수를 카운트
print(num.count(5))
# pop으로 마지막 데이터 출력추 제거
print(num.pop())
# num 출력
print(num)
# 인덱스 2번 데이터를 pop으로 출력하고 num출력
print(num.pop(2)); print(num)
