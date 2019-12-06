from bs4 import BeautifulSoup
import urllib.request as req


url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
# print(soup)
# li 테그 아래 a 태그 의 text 를 읽어 올때
# ul > li a  -> 한칸띄우고 쓰는 테그는 경우 하위 모든 자식들 모두 중에서 검색..
list = soup.select('ul > li a') # ui의 자식 li 중에 a 태그에 있는 글자
for i in list:
    print("-", i.string)