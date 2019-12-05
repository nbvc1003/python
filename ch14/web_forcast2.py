import sys
import urllib.request as req
import urllib.parse as parse
print('지역번호를 입력하세요')

regionNumber = input()
api = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {'stnId':regionNumber}
params = parse.urlencode(values)
url= api+"?"+params
data = req.urlopen(url).read()
text = data.decode('utf-8')
print(text)