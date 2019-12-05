import urllib.request
import urllib.parse
api = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

values = {'stnId':'108'}
params = urllib.parse.urlencode(values)
# url = api+"?"+"stnId=108"
url = api+"?"+params # 위와 동일하다.

print(url)
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)