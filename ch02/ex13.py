

# 와우 다음시간이 점심

# 20칸 확보 왼쪽/오른쪽/중앙 정렬
# 위와 같은데 빈칸 | 를 채우기
# 45% 입니다. 출력
# 2.4567 을 소수점 2자리 출력 format 사용

s1 = "와우 다음시간이 점심"
print("{0:|<20}".format(s1))
print("{0:|>20}".format(s1))
print("{0:|^20}".format(s1))

print("%d%% 입니다."%(45))
print("{0:0.2f}".format(2.4567))
