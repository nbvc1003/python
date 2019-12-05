from bs4 import BeautifulSoup

# id 하나, class 복수
html = """
    <html>
        <body>
        <div id="meign">
            <h1>위키북스 도서</h1>
            <ul class="items">
                <li>R</li>
                <li>파이썬</li>
                <li>통계</li>
                <li>대박</li>
            </ul>
        </div>
        </body>
    </html>
"""

soup = BeautifulSoup(html, "html.parser")
#  조건식 의미 :  '#' : id , '.' : class , '>' : 하위
# div 테그 안에 (#) id가 meign 인 테그 자식중 h1 태그 사이의 문자열
h1 = soup.select_one("div#meign > h1").string
# div 테그중 id = meign 중 하위 ul중 class = items 내부 li 들 선택
list = soup.select("div#meign > ul.items > li")
print(h1)
for i in list:
    print(i.string)

print("=====================================")
h2 = soup.find("h1").string
print(h2)
list2 = soup.find_all("li")
for i in list2:
    print(i.string)





