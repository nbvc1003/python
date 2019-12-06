from bs4 import BeautifulSoup
fp = open('pet.html', encoding='utf-8')

soup = BeautifulSoup(fp, 'html.parser')
sel = lambda x:soup.select_one(x).string

print(soup.select_one("li.g3").string)
print(sel('li:nth-of-type(3)'))