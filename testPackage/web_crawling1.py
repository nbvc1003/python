from bs4 import BeautifulSoup # XML, HTML
import urllib.request

url = "http://www.inven.co.kr/board/destinyguardians/5051"
res = urllib.request.urlopen(url)
data = res.read()
# byte 데이터 -> text
html = data.decode("utf-8")
# print(text)
soup = BeautifulSoup(html, 'html.parser')

##powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody

# tables = soup.find_all('div')
# tables = soup.find("tr") #특정 테그만 읽어 올때
table1 = soup.select("tr.ls > td.bbsSubject > a.sj_ln")
table2 = soup.select("tr.ls tr tr2")
print(table1)
print(len(table1))
# print(len(tables))
# for t in tables:
#     print(t.attrs['name'])