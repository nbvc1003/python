
# 빈리스트 만들기
numbers = [] # numbers 에 자연수 1, 10까지 추가
numbers[:] = range(1,11) # 리스트에 1~11 의 값을 넣어 준다. 
print(numbers)
#홀수 제거
# del numbers[::2]
# print(numbers)

# 짝수 제거
del numbers[1::2]
print(numbers)

# numbers 의 인덱스 0 자리에 20을 삽입
numbers[0] = 20


# numbers를 정렬 해라
numbers.sort()







