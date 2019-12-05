from bs4 import BeautifulSoup # XML, HTML 해석기능


html = """
    <html>
        <body>
            <h1>스크레이핑이란</h1>
            <p>웹페이지를 분석하는 것</p>
            <p>원하는 부분을 추출하는 것</p>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')
# 계층형 구조에 맞춰서 읽는다.

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
# x.string  : <x> ~ </x> 테그사이의 문장
print(h1.string)
print(p1.string)
print(p2.string)
print("============================================")
# 특정태그를 전부 가져올때 
ps = soup.find_all('p')
for p in ps:
    print('p =', p.string)





