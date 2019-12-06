from bs4 import BeautifulSoup


fp = open('fruit.html', encoding='utf-8')

soup = BeautifulSoup(fp, 'html.parser')

#sel = lambda x:soup.select_one(x).string


print(soup.select("li.black")[1].string)
print(soup.select(".black")[1].string)
print(soup.select("#ve-list li.black")[1].string)
print(soup.select("#ve-list li[data-lo='us']")[1].string)

print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("li:nth-of-type(4)")[1].string)

# find
# dic 형식으로 조건을 추가해서 검색 할 수 있다.
cond = {'data-lo':'us','class':'black'}
print("find() 사용 : ", soup.find('li', cond).string)

