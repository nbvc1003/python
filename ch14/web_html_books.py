from bs4 import BeautifulSoup
fp = open('books.html', encoding='utf-8')

soup = BeautifulSoup(fp, 'html.parser')
sel = lambda x:soup.select_one(x).string
# 아래 조건식이 전부 같은 결과
print(sel('#nu')) # id nu
print(sel('li#nu')) # li 안에 id가 nu
print(sel('ul > li#nu')) # ul자식으로 li안에 id 가 nu
print(sel('#bible #nu')) # id 가 bible 후손으로 id가 nu
print(sel('ul#bible #nu')) # ul안에  id 가 bible 후손으로 id가 nu
print(sel('#bible > #nu')) # id가 bible 자식으로 id 가 nu
print(sel('li[id="nu"]')) # li태그 안에 id 속성이 nu
print(sel("li:nth-of-type(4)")) # li 형식 중에서 4번째 요소 (교안 참고 .)

print(soup.select("li")[3].string) # css형식 li 순서로 index 번호가 3
print(soup.find_all("li")[3].string) # html형식