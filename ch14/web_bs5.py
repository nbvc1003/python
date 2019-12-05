from bs4 import BeautifulSoup
import urllib.request as req

url = "https://blog.naver.com/himuraea0"
res = req.urlopen(url) # 해당하는 주소의 html을 다운받아서 res저장
soup = BeautifulSoup(res, 'html.parser')

# print(soup)

title = soup.find("title").string # 테그 사이 문자
print("제목 :", title)
