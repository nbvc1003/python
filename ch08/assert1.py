
print("숫자를 입력하세요")

num = int(input())
margin = num * 0.2

# 중단 조건 (디버그용 ,테스트용)
assert margin > 10, "마진이 작습니다."

print("입력한 숫자는 {} 입니다.".format(num))