# 데이터 가져오기
import requests

r = requests.get("http://api.aoikujira.com/time/get.php")

# 텍스트 형식으로 데이터 추출하기
text = r.text # 일반 데이터, 문서
print(text)
# 바이너리 형식으로 데이터 추출하기
bin = r.content # 바이너리 데이터, 음악, 그림
print(bin)


