
import requests
import bs4
#powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody > tr:nth-child(8)
#table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody
#powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody > tr:nth-child(8)
# div > div > div > div > main > c-wiz > div > div > div
spp = 'table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr'

url = "http://www.inven.co.kr/board/destinyguardians/5051"

resp = requests.get(url)

soup = bs4.BeautifulSoup(resp.text, 'lxml')
#soup = bs4.BeautifulSoup(resp.text, 'html.parser')
print(len(soup))
items = soup.select(spp)

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