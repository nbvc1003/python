from bs4 import BeautifulSoup


fp = open('fruit.html', encoding='utf-8')

soup = BeautifulSoup(fp, 'html.parser')

#sel = lambda x:soup.select_one(x).string

print(soup.select_one("ul#fr-list > li.yellow").string)

# 클래스 여러개의 조건 [조건1][조건2]
print(soup.select_one("ul#fr-list > li[class='yellow'][data-lo='us']").string)

print(soup.select_one("li.yellow").string)

print(soup.select_one('#fr-list li:nth-of-type(3)').string)

# 상세 조건을 부여 하여 검색 할때 사용 한다.
cond = {"data-lo":"us","class":"yellow"}
print(soup.find("li", cond).string)
