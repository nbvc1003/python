import requests
import bs4
import pandas as pd

# url = 'https://www.google.com/search?newwindow=1&biw=1552&bih=919&tbm=nws&sxsrf=ACYBGNQUIJi75WqnRc1LGCehCpWtuFsU7g%3A1574233256572&ei=qOTUXevIIqm9hwPI0ofwDQ&q=%EB%8C%80%ED%95%9C%ED%95%AD%EA%B3%B5&oq=%EB%8C%80%ED%95%9C%ED%95%AD%EA%B3%B5&gs_l=psy-ab.3..0l10.3078.5205.0.5664.11.9.0.1.1.0.153.713.1j5.6.0....0...1c.1j4.64.psy-ab..5.6.618....0.n5lk46F-QPU'
url = "https://news.google.com/?tab=wn1&hl=ko&gl=KR&ceid=KR:ko"

resp = requests.get(url)

soup = bs4.BeautifulSoup(resp.text, 'lxml')

#rso > div > div:nth-child(1)
#rso > div > div:nth-child(1)
# items = soup.select(' div > div > a')
items = soup.select('div > div > div > div > main > c-wiz > div > div > div > article > h3 > a')
# div > div > div > div > main > c-wiz > div > div > div > article > h3 > a
# div > div > div > div > main > c-wiz > div > div

print(len(items))

titles = []
links = []
for item in items:
    titles.append(item.text)
    links.append(item.get('href'))

for i in titles:
    print(i)

for i in links:
    print(i)



