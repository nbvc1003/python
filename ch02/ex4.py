
str = "할로윈 그게 뭐야 대박"

# 몇자 ?
print(len(str))
# 그게 라는 단어가 포함 여부
print("그게" in str)
# 위 문장르 3번 반복
print(str *3)
# 할 자로  시작하나?
print(str.startswith("할"))

# 뭐야라는 단어의 위치
print(str.find("뭐야")) # 앞에서 부터 찾는다.
# 윈를 뒤에서 부터 확인
print(str.rfind("윈")) # 뒤에서 부터 찾는다.
print(str.find("윈"))

# 로 라는 단어의 갯수
print(str.count("로"))