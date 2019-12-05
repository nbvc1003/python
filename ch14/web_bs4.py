from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url) # 해당하는 주소의 html을 다운받아서 res저장
soup = BeautifulSoup(res, 'html.parser')

#print(soup)

title = soup.find("title").string # 테그 사이 문자
wf = soup.find('wf').string
print("제목 :", title)
print("내용 \n", wf)

